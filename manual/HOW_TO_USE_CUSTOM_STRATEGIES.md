# 🎯 How Users Can Input Their Own Strategies

## Quick Answer

**YES! Users can write strategies in plain English - NO need to learn the DSL!**

The system automatically converts English to the DSL, parses it, generates Python code, and runs backtests.

---

## The Simple Pipeline

```
Your English Strategy
    ↓
Natural Language Parser (NL Parser)
    ↓
Domain Specific Language (DSL)
    ↓
Abstract Syntax Tree (AST)
    ↓
Python Code
    ↓
Backtest Results
```

---

## How It Works

### Step 1: Write Your Strategy in English

```python
strategy = """
Buy when the close price is above the 20-day moving average 
and the volume is greater than 1 million.
Sell when the close price drops below the 50-day moving average.
"""
```

### Step 2: Let the System Convert It

```python
from engine.nl_parser import nl_to_dsl

dsl = nl_to_dsl(strategy)
# Result:
# Entry: "ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000"
# Exit:  "EXIT: CLOSE LT SMA(CLOSE, 50)"
```

### Step 3: Parse It to AST

```python
from engine.dsl_parser import parse_dsl_to_ast

ast = parse_dsl_to_ast(f"{dsl['entry']} {dsl['exit']}")
```

### Step 4: Generate Python Code

```python
from engine.code_generator import generate_python_strategy

python_code = generate_python_strategy(ast)
```

### Step 5: Run Backtest

```python
from engine.backtester import run_backtest
from engine.data_utils import load_data

df = load_data()
results = run_backtest(df, signals)
```

---

## Supported English Phrases

### Price Fields
```
- "close price" or just "close"    → CLOSE
- "volume"                          → VOLUME
- "high"                            → HIGH
- "low"                             → LOW
- "open"                            → OPEN
```

### Comparison Operators
```
- "above"  or "greater than"       → GT
- "below"  or "less than"          → LT
- "equal to"                        → EQ
```

### Indicators
```
- "20-day moving average"           → SMA(CLOSE, 20)
- "50 day moving average"           → SMA(CLOSE, 50)
- "RSI(14)"                         → RSI(CLOSE, 14)
```

### Logic
```
- "and"                             → AND
- "or"                              → OR
```

### Entry/Exit Actions
```
- "buy when" or "enter when"       → ENTRY:
- "sell when" or "exit when"       → EXIT:
```

---

## Real Examples

### Example 1: Moving Average Crossover

**English:**
```
Buy when close is above the 50-day moving average.
Sell when close goes below the 20-day moving average.
```

**Converted to DSL:**
```
ENTRY: CLOSE GT SMA(CLOSE, 50)
EXIT: CLOSE LT SMA(CLOSE, 20)
```

**Generated Python (simplified):**
```python
sma_50 = calculate_sma(df['CLOSE'], 50)
sma_20 = calculate_sma(df['CLOSE'], 20)

entry_signals = df['CLOSE'] > sma_50
exit_signals = df['CLOSE'] < sma_20
```

---

### Example 2: Volume Breakout

**English:**
```
Buy when volume is greater than 2 million and close is above the 20-day average.
Sell when volume drops below 500000.
```

**Converted to DSL:**
```
ENTRY: VOLUME GT 2000000 AND CLOSE GT SMA(CLOSE, 20)
EXIT: VOLUME LT 500000
```

---

### Example 3: Simple Momentum

**English:**
```
Enter when close is above 30-day moving average.
Exit when close falls below 10-day moving average.
```

**Converted to DSL:**
```
ENTRY: CLOSE GT SMA(CLOSE, 30)
EXIT: CLOSE LT SMA(CLOSE, 10)
```

---

## How the NL Parser Works

The Natural Language Parser uses **pattern matching** to convert English to DSL:

1. **Identifies price fields** - Finds "close", "volume", etc.
2. **Finds comparisons** - Detects "above", "below", "greater than", etc.
3. **Extracts indicators** - Recognizes "20-day moving average", "RSI(14)"
4. **Converts logic** - Handles "and" and "or" statements
5. **Distinguishes entry/exit** - Separates "buy when" from "sell when"
6. **Removes filler words** - Strips out articles and conjunctions
7. **Formats as DSL** - Outputs valid DSL syntax

---

## Running Your Own Strategy

### Using `custom_strategy.py`

```bash
python custom_strategy.py
```

This runs 3 example strategies and shows:
- Your English input
- The converted DSL
- The generated Python code
- Backtest results

### Creating Your Own

Edit `custom_strategy.py` and add your strategy:

```python
# At the bottom of the file, uncomment:
my_strategy = """
Enter when close is above 100-day moving average.
Exit when close drops below 50-day moving average.
"""
run_custom_strategy(my_strategy)
```

Then run:
```bash
python custom_strategy.py
```

---

## Limitations & Tips

### What Works
- ✅ Simple conditions: "close above 20-day average"
- ✅ Combined conditions: "close above 20-day AND volume above 1 million"
- ✅ Multiple indicators: SMA and RSI
- ✅ Any combination of AND/OR logic

### What Doesn't Work (Yet)
- ❌ Time-based rules: "Buy on Monday" or "Buy after 3PM"
- ❌ Previous values: "If yesterday's close was higher than today"
- ❌ Complex calculations: "Buy if (close - open) > 10"
- ❌ Position sizing: "Buy 100 shares" or "Risk 2% per trade"

### Tips for Best Results

1. **Be specific with numbers**
   ```
   Good:   "above 20-day moving average"
   Bad:    "above the average"
   
   Good:   "volume above 1 million"
   Bad:    "high volume"
   ```

2. **Use standard comparison phrases**
   ```
   Good:   "above", "below", "greater than", "less than"
   Bad:    "higher than", "lower than", "exceeds"
   ```

3. **Be clear about entry and exit**
   ```
   Good:   "Buy when... Sell when..."
   Bad:    "Buy when... and then close the position"
   ```

4. **Use correct indicator format**
   ```
   Good:   "20-day moving average", "RSI(14)"
   Bad:    "20 day ma", "RSI 14"
   ```

---

## How to Extend It

### Adding Support for More Phrases

Edit `engine/nl_parser.py`:

```python
# Add to OPERATOR_MAP for new comparisons:
OPERATOR_MAP = {
    r'\b(is\s+)?above\b': ' GT ',
    r'\b(is\s+)?higher\s+than\b': ' GT ',  # NEW!
    # ... more ...
}

# Add to FIELD_MAP for new price fields:
FIELD_MAP = {
    r'\bclose\s*price\b': 'CLOSE',
    r'\badj.*close\b': 'CLOSE',  # NEW! Matches "adjusted close"
    # ... more ...
}
```

### Adding New Indicators

Edit `engine/nl_parser.py`:

```python
INDICATOR_PATTERNS = [
    (r'(\d+)\s*(-day)?\s*moving\s*average', r'SMA(CLOSE, \1)'),
    (r'RSI\s*\((\d+)\)', r'RSI(CLOSE, \1)'),
    (r'(\d+)\s*-?day\s*exponential\s*average', r'EMA(CLOSE, \1)'),  # NEW!
    # ... more ...
]
```

Then implement the indicator in `engine/data_utils.py`:

```python
def calculate_ema(series, period):
    """Calculate Exponential Moving Average"""
    return series.ewm(span=period, adjust=False).mean()
```

---

## The Bigger Picture

This NL → DSL → AST → Code pipeline is **generalized**:

- **Same pipeline for any domain** - Could convert to SQL, JavaScript, other languages
- **Easy to extend** - Just add more patterns to the NL parser
- **Accurate** - Everything goes through a proper AST
- **Testable** - Each stage can be validated independently

The beauty is: **Users speak naturally, but the code runs deterministically.**

---

## Summary

| Feature | Status | Details |
|---------|--------|---------|
| Plain English input | ✅ Fully working | Just write naturally |
| Automatic conversion | ✅ Fully working | NL → DSL → AST → Code |
| Backtesting | ✅ Fully working | Runs on sample data |
| Custom strategies | ✅ Fully working | Use `custom_strategy.py` |
| Extendable | ✅ Easy | Add patterns to NL parser |

---

**Bottom Line:** Users don't need to learn DSL syntax at all. They can write strategies in English, and the system handles all the conversion automatically. Try `python custom_strategy.py` to see it in action!
