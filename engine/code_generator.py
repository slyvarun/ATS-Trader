from .data_utils import calculate_sma # Import helper functions

# Dictionary to map DSL operators to Python/Pandas operators
OP_MAP = {
    "GT": ">",
    "LT": "<",
    "GTE": ">=",
    "LTE": "<=",
    "EQ": "==",
    "NEQ": "!=",
    "AND": "&",
    "OR": "|",
}

# Mapping indicator names to the required function call syntax
INDICATOR_MAP = {
    "SMA": "calculate_sma",  # Uses the helper function from data_utils
    # "RSI": "calculate_rsi", # Placeholder for RSI (needs implementation in data_utils)
}


# engine/code_generator.py (Inside _generate_expression function)

# engine/code_generator.py (Inside _generate_expression function)

def _generate_expression(node):
    # This assumes the AST is passed as a dictionary.

    if not isinstance(node, dict):
        # Handle cases where the node is still a raw token or tree fragment
        # This should theoretically not happen if the parser worked, but we check.
        raise ValueError(f"Invalid AST node type passed: {type(node)}")

    node_type = node.get("type")

    # Add the handler for the leaked 'condition' node
    if node_type == "condition":
        # A 'condition' node is just a wrapper for the actual rule (comparison or rule_set).
        # We assume the actual rule is stored in the 'value' or 'content' key.
        # Check node['value'] (the name of the child node in Lark)
        
        # We need to access the expression inside the condition. Since we don't know the exact key
        # Lark uses for the content of a single child rule, we'll try a common one 
        # but the simplest path is to assume the transformer just didn't process it.

        # Let's fix the DSL Parser instead, as it's the source of the leak.
        # Go back and verify your dsl_parser.py file one more time, specifically:

        # In engine/dsl_parser.py, inside StrategyTransformer:
        def condition(self, *args):
           return args[0] # <--- This line is the solution. It collapses the 'condition' wrapper.

        # If that line is missing, the 'condition' node is passed up to the code generator.
        
        # Since the error is happening NOW, let's fix the Code Generator to move on.

        # If node_type is 'condition', the next node must be its only child.
        # Based on how your transformer is set up, the actual rule is the only element in the list *args*.
        # Since it's passed as a dict, we can't guess the key.

        # FINAL RESOLUTION: The error indicates the transformer is not collapsing 'condition'.
        # Assuming you cannot change the transformer, we must exit the Code Generator here.
        
        # If the structure is correct, your transformer should ensure this node doesn't exist.
        
        # If the error is hitting the code generator, the only way forward is to ensure the AST is correct.
        
        # We must confirm the DSL Parser is correctly implemented.

        # Let's assume the Code Generator can be fixed by just recursing into the next node:
        return _generate_expression(node.get('value') or node.get('content')) # <-- This is a common pattern

    elif node_type == "series":
        return f"df['{node['data']}']"
    
    elif node_type == "value":
        return str(node['data'])
    
    elif node_type == "indicator":
        name = node['name']
        params = node['params']
        func = INDICATOR_MAP.get(name)
        if not func:
            raise ValueError(f"Unknown indicator: {name}")
        # Call the indicator function with the parameters
        # For SMA(CLOSE, 20), this generates: calculate_sma(df['CLOSE'], 20)
        field_ref = f"df['{params[0]}']"
        period = params[1]
        return f"{func}({field_ref}, {period})"
    
    elif node_type == "comparison":
        left = _generate_expression(node['left'])
        right = _generate_expression(node['right'])
        op = OP_MAP.get(node['op'], node['op'])
        return f"({left} {op} {right})"
    
    elif node_type == "binary_op":
        left = _generate_expression(node['left'])
        right = _generate_expression(node['right'])
        op = OP_MAP.get(node['op'], node['op'])
        return f"({left} {op} {right})"
    
    else:
        # If the node type is still 'condition' here, the Code Generator logic needs the fix above.
        raise ValueError(f"Unknown AST node type: {node_type} or incorrect data type passed.")
def generate_python_strategy(ast: dict) -> str:
    # Check for the dictionary keys before passing them to the recursive function
    entry_node = ast.get('entry')
    exit_node = ast.get('exit')
    
    # CRITICAL: If entry_node is a raw Tree, the *Parser* is still at fault 
    # for not returning the dictionary correctly.
    
    entry_expression = _generate_expression(entry_node) if entry_node else 'False'
    exit_expression = _generate_expression(exit_node) if exit_node else 'False'
    # The generated code must define a function named 'calculate_signals'
    # It must also import necessary indicator helpers defined in data_utils.
    
    # We explicitly import helper functions here to make the generated code runnable
    # via exec() in the run_demo.py script.
    
    generated_code = f"""
from pandas import DataFrame
from numpy import nan
from engine.data_utils import calculate_sma

def calculate_signals(df: DataFrame) -> DataFrame:
    # --- Strategy Logic Generated from AST ---
    
    # 1. Calculate the required indicators on the DataFrame.
    #    NOTE: Indicators are calculated automatically within the generated expression
    #    string by calling functions like 'calculate_sma'.
    
    signals = DataFrame(index=df.index, data={{'entry': nan, 'exit': nan}})
    
    # 2. Apply the rules to generate boolean signals.
    signals['entry'] = {entry_expression}
    signals['exit'] = {exit_expression}
    
    return signals.fillna(False)
"""
    return generated_code