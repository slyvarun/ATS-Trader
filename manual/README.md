# ✏️ Manual Strategy Builder

**Edit Python files and run them to test trading strategies!**

## Quick Start

### Option 1: Edit and Run

Edit `custom_strategy.py`:
```python
my_strategy = """
Buy when close is above 20-day moving average.
Sell when close drops below 50-day moving average.
"""
run_custom_strategy(my_strategy)
```

Then run:
```bash
python custom_strategy.py
```

### Option 2: Create Your Own File

Create `my_strategy.py`:
```python
from engine.nl_parser import nl_to_dsl
from engine.dsl_parser import parse_dsl_to_ast
from engine.code_generator import generate_python_strategy
from engine.backtester import run_backtest
from engine.data_utils import load_data
from numpy import nan

strategy = """
Enter when close is above 100-day moving average.
Exit when close falls below 50-day moving average.
"""

dsl = nl_to_dsl(strategy)
dsl_text = f"{dsl['entry']} {dsl['exit']}"
ast = parse_dsl_to_ast(dsl_text)
code = generate_python_strategy(ast)
df = load_data()

exec_globals = {
    'DataFrame': __import__('pandas').DataFrame,
    'nan': nan,
    'calculate_sma': __import__('engine.data_utils', fromlist=['calculate_sma']).calculate_sma,
}
exec_scope = {}
exec(code, exec_globals, exec_scope)
signals = exec_scope['calculate_signals'](df)
results = run_backtest(df, signals)

print(results)
```

Then run:
```bash
python my_strategy.py
```

## Files in This Folder

- **custom_strategy.py** - Template with 3 example strategies
- **custom_strategy_example.py** - Alternative examples
- **HOW_TO_USE_CUSTOM_STRATEGIES.md** - Detailed guide
- **USER_INPUT_GUIDE.md** - Quick reference

## Workflow

1. Open `custom_strategy.py` in your editor
2. Find the strategy section (around line 155)
3. Edit the strategy in English
4. Save the file
5. Run: `python custom_strategy.py`
6. See results

## Example Strategies

### Strategy 1: Simple Moving Average
```
Buy when close is above 20-day moving average.
Sell when close drops below 50-day moving average.
```

### Strategy 2: With Volume Filter
```
Buy when close is above 30-day moving average and volume is above 1 million.
Sell when close drops below 30-day moving average.
```

### Strategy 3: Breakout
```
Enter when close is above 50-day moving average.
Exit when close falls below 20-day moving average.
```

## Supported Phrases

- **Prices:** close, volume, high, low, open
- **Operators:** above, below, greater than, less than, equal to
- **Indicators:** 20-day moving average, RSI(14)
- **Logic:** and, or
- **Entry/Exit:** buy/enter when, sell/exit when

## When to Use Manual Mode

Use this when you:
- Want to use your favorite code editor
- Need to save multiple strategies as separate files
- Want more control over the execution
- Prefer editing files over interactive input

## Tips

✅ **Do:**
- Save each strategy as a separate file
- Add comments to explain your strategy
- Use meaningful file names (e.g., `sma_strategy.py`)
- Test strategies in small batches

❌ **Don't:**
- Edit the engine code (in parent folder)
- Delete core files by accident
- Mix manual and interactive runs

## Documentation

For detailed guides on writing strategies, see:
- **HOW_TO_USE_CUSTOM_STRATEGIES.md** - Complete reference
- **USER_INPUT_GUIDE.md** - Quick examples

## Quick Test

To run the examples:
```bash
python custom_strategy.py
```

This shows 3 working strategies automatically! 🚀
