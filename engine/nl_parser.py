# engine/nl_parser.py

import re
from typing import Dict

# --- Mapping Dictionaries ---

# Maps English phrases to DSL FIELD tokens. Prioritizes multi-word phrases.
FIELD_MAP = {
    r'\bclose\s*price\b': 'CLOSE',
    r'\bvolume\b': 'VOLUME',
    r'\bhigh\b': 'HIGH',
    r'\slow\b': 'LOW',
    r'\bopen\b': 'OPEN',
}

# Maps English operators/comparisons to DSL OPERATOR tokens (GT, LT, etc.)
# IMPORTANT: Spaces are added around the operator to ensure clean separation during tokenization.
OPERATOR_MAP = {
    r'\b(is\s+)?above\b': ' GT ',
    r'\b(is\s+)?greater\s+than\b': ' GT ',
    r'\b(is\s+)?below\b': ' LT ',
    r'\b(is\s+)?less\s+than\b': ' LT ',
    r'\b(is\s+)?equal\s+to\b': ' EQ ',
}

# Maps indicator phrases to their DSL syntax.
INDICATOR_PATTERNS = [
    # Matches '20-day moving average' or '50 day moving average' -> SMA(CLOSE, 20)
    (r'(\d+)\s*(-day)?\s*moving\s*average', r'SMA(CLOSE, \1)'),
    # Matches 'RSI(14)' or 'RSI (14)' -> RSI(CLOSE, 14)
    (r'RSI\s*\((\d+)\)', r'RSI(CLOSE, \1)'), 
]


# engine/nl_parser.py (UPDATED)

# ... (FIELD_MAP, OPERATOR_MAP, INDICATOR_PATTERNS remain the same) ...

def _tokenize_rule(rule_text: str) -> str:
    """
    Replaces English phrases within a single rule segment with standardized DSL tokens,
    and aggressively removes filler words.
    """
    
    # 1. Normalize and lowercase the text
    text = rule_text.lower()
    
    # 2. Replace Indicators FIRST (e.g., '20-day moving average' -> 'SMA(CLOSE, 20)')
    # This must happen before removing words like "day" and "average"
    for pattern, dsl_format in INDICATOR_PATTERNS:
        text = re.sub(pattern, dsl_format, text)
        
    # 3. Replace simple fields (e.g., 'close price' -> 'CLOSE')
    for pattern, dsl_field in FIELD_MAP.items():
        text = re.sub(pattern, dsl_field, text)

    # 4. Replace comparison operators (e.g., 'is above' -> ' GT ')
    for pattern, dsl_op in OPERATOR_MAP.items():
        text = re.sub(pattern, dsl_op, text)

    # 5. Replace logic connectors (ensure they are capitalized for the DSL)
    text = re.sub(r'\band\b', ' AND ', text)
    text = re.sub(r'\bor\b', ' OR ', text)
    
    # 6. Replace number phrasing (e.g., '1 million' -> '1000000', '2 million' -> '2000000')
    text = re.sub(r'(\d+)\s*million', lambda m: str(int(m.group(1)) * 1000000), text)
    
    # 7. AGGRESSIVE FILLER REMOVAL (NOW AFTER INDICATORS)
    text = re.sub(r'\b(the|a|an|is|when|if|than|of|by|drops|falls|goes|moves|gets|rises|day|average)\b', ' ', text)
    
    # 8. FINAL CLEANUP AND CASE CORRECTION
    # Correct case for all DSL tokens (FIELDS, LOGIC, etc.)
    text = text.upper()
    
    # Critical: Remove only periods. We must KEEP the commas inserted by the INDICATOR_PATTERNS.
    text = text.replace('.', '') 
    
    # Remove excessive spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove spaces around parentheses (important for indicators)
    text = text.replace('( ', '(').replace(' )', ')')
    
    return text

# ... (nl_to_dsl function remains the same) ...

def nl_to_dsl(nl_input: str) -> Dict[str, str]:
    """
    Parses a Natural Language input string, separates it into Entry/Exit segments,
    and converts each segment into a final DSL rule string.
    """
    
    # --- Split NL Input into Entry and Exit Segments ---
    
    # Use 'buy when', 'enter when' for entry, and 'exit when', 'sell when' for exit.
    
    entry_rule_text = ""
    exit_rule_text = ""
    
    # Look for a complete instruction set
    full_match = re.search(r'(buy|enter)\s+when\s+(.*?)\s+(exit|sell)\s+when\s+(.*)', nl_input.lower(), re.DOTALL)
    
    if full_match:
        entry_rule_text = full_match.group(2).strip()
        exit_rule_text = full_match.group(4).strip()
    else:
        # If no explicit EXIT is found, assume the whole text is for entry
        match_entry_only = re.search(r'(buy|enter)\s+when\s+(.*)', nl_input.lower(), re.DOTALL)
        if match_entry_only:
            entry_rule_text = match_entry_only.group(2).strip()
        else:
            # Fallback: assume the entire input is the rule text if no keywords are found
            entry_rule_text = nl_input.lower()


    # --- Tokenize Segments and Format DSL ---
    
    dsl_entry_logic = _tokenize_rule(entry_rule_text)
    dsl_exit_logic = _tokenize_rule(exit_rule_text)
    
    # Final DSL Formatting
    # The DSL grammar requires both ENTRY and EXIT rule_sets. If no explicit
    # exit logic was provided, emit a harmless always-false comparison that
    # parses correctly (e.g., 0 > 1) instead of the word FALSE which was not
    # part of the grammar.
    exit_clause = dsl_exit_logic if dsl_exit_logic else "0 > 1"
    return {
        'entry': f"ENTRY: {dsl_entry_logic}",
        'exit': f"EXIT: {exit_clause}"
    }