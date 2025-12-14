# engine/dsl_parser.py
from lark import Lark, Transformer, v_args
from typing import Dict, Any

# --- DSL GRAMMAR DEFINITION ---
# This grammar is specifically designed to resolve the ambiguity between FIELDS and INDICATORS.
GRAMMAR = r"""
    start: strategy

    strategy: "ENTRY:" rule_set "EXIT:" rule_set

    // RULE_SET handles the combination of rules with AND/OR logic
    rule_set: condition (LOGIC_OP condition)*
    
    // CONDITION can be a simple comparison or a nested rule set
    condition: comparison
             | "(" rule_set ")"

    comparison: expression OPERATOR expression

    // EXPRESSION can be a price series, an indicator, or a number
    expression: FIELD 
              | indicator 
              | NUMBER

    // INDICATOR_NAME is used instead of generic IDENTIFIER to prevent token conflicts
    indicator: INDICATOR_NAME "(" FIELD "," NUMBER ")"

    // --- TERMINALS (Tokens) ---
    LOGIC_OP: "AND" | "OR"
    // Operators include word-based (GT) and symbol-based (>).
    OPERATOR: ">=" | "<=" | ">" | "<" | "==" | "!=" | "GT" | "LT" | "GTE" | "LTE"

    // Explicitly define indicator function names to avoid conflict with fields
    INDICATOR_NAME: "SMA" | "RSI"

    // FIELD names must be uppercase
    FIELD: "CLOSE" | "OPEN" | "HIGH" | "LOW" | "VOLUME" 

    %import common.SIGNED_NUMBER -> NUMBER
    %import common.WS
    %ignore WS
"""

@v_args(inline=True) # Allows rules to return their components directly
class StrategyTransformer(Transformer):
    """Transforms the parsed Lark Tree into the final Abstract Syntax Tree (AST) structure."""

    def __init__(self):
        super().__init__()
        self.ast = {"entry": [], "exit": []}

    def strategy(self, entry_rules, exit_rules):
        """Called upon successful parsing of the entire strategy."""
        self.ast["entry"] = entry_rules
        self.ast["exit"] = exit_rules
        return self.ast
    def start(self, *items):
        return items[0]
    def rule_set(self, *items):
        """Converts a sequence of conditions and logical operators into a nested logical tree."""
        if len(items) == 1:
            return items[0] # Single condition
        
        # Build a nested logical tree (e.g., A AND B AND C)
        left = items[0]
        for op, right in zip(items[1::2], items[2::2]):
            left = {
                "type": "binary_op",
                "op": str(op),
                "left": left,
                "right": right
            }
        return left

    def condition(self, item):
        """Passes through the condition content (either a comparison or nested rule_set)."""
        return item

    def comparison(self, left, op, right):
        """Builds a comparison node."""
        return {
            "type": "comparison",
            "op": str(op),
            "left": left,
            "right": right
        }

    def indicator(self, name, field, period):
        """Builds an indicator function node (e.g., SMA(CLOSE, 20))."""
        return {
            "type": "indicator",
            "name": str(name),
            "params": [str(field), int(period)]
        }

    def expression(self, item):
        """Handles the final output type for a simple token (Field, Indicator, or Number)."""
        if not isinstance(item, dict):
            # This handles the immediate terminal token (NUMBER or FIELD)
            try:
                # Try to convert token to float (for NUMBER)
                return {"type": "value", "data": float(item)}
            except ValueError:
                # If conversion fails, it's a FIELD (Series)
                return {"type": "series", "data": str(item)}
        return item # Returns the dictionary for an 'indicator' node

    # --- Transformer methods for Terminals (pass-through/type-casting) ---
    NUMBER = lambda self, n: str(n)
    FIELD = lambda self, f: str(f)
    INDICATOR_NAME = lambda self, i: str(i)
    LOGIC_OP = lambda self, op: str(op)

# --- Public Interface ---

# Globalize the parser instance to prevent "Rule defined more than once" errors
DSL_PARSER = Lark(GRAMMAR, parser='lalr')

def parse_dsl_to_ast(dsl_text: str) -> Dict[str, Any]:
    """
    Parses DSL text and builds the AST using the pre-initialized global parser.
    """
    
    try:
        # Step 1: Parse the DSL text into a raw Lark Tree
        tree = DSL_PARSER.parse(dsl_text)
        
        # Step 2: Transform the Tree into your final Python Dictionary AST
        # The StrategyTransformer's 'strategy' method returns the dict: {"entry":..., "exit":...}
        ast = StrategyTransformer().transform(tree) 
        
        # Step 3: RETURN THE DICTIONARY (the AST)
        return ast 
        
    except Exception as e:
        # Raises informative errors for invalid syntax
        raise ValueError(f"DSL Syntax Error: {e}")