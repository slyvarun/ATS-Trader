# 🎮 Interactive Strategy Builder

## How to Use

### Method 1: Interactive Menu (Recommended for Beginners)

```bash
python interactive_strategy.py
```

This opens an interactive menu:
```
======================================================================
MENU
======================================================================
1. Enter your strategy
2. See example strategies
3. See supported phrases
4. Exit

Choose option (1-4): _
```

**What you can do:**
- **Option 1:** Type your own strategy and watch it execute live
- **Option 2:** See 3 example strategies
- **Option 3:** Learn what English phrases are supported
- **Option 4:** Exit the program

---

### Method 2: Quick Test (Command Line Argument)

```bash
python interactive_strategy.py "Buy when close is above 20-day moving average. Sell when close drops below 50-day moving average."
```

This runs your strategy immediately without the menu!

---

## 🎯 Real Example

### Using Interactive Menu

1. Run:
```bash
python interactive_strategy.py
```

2. You'll see:
```
======================================================================
INTERACTIVE TRADING STRATEGY BUILDER
======================================================================

Welcome! You can describe trading strategies in plain English.
The system will convert it to code and test it automatically.


======================================================================
MENU
======================================================================
1. Enter your strategy
2. See example strategies
3. See supported phrases
4. Exit

Choose option (1-4): 
```

3. Type `1` and press Enter

4. System asks for your strategy:
```
======================================================================
ENTER YOUR STRATEGY
======================================================================

Describe your strategy in English.
Example:
  "Buy when close is above 20-day moving average and volume is above 1 million.
   Sell when close drops below 50-day moving average."

Start typing (press Enter twice when done):
----------------------------------------------------------------------
_
```

5. Type your strategy (press Enter twice when done):
```
Buy when close is above 30-day moving average and volume is above 1 million.
Sell when close drops below 20-day moving average.

_
```

6. System processes it:
```
----------------------------------------------------------------------
YOUR STRATEGY
----------------------------------------------------------------------
Buy when close is above 30-day moving average and volume is above 1 million.
Sell when close drops below 20-day moving average.

----------------------------------------------------------------------
STEP 1: CONVERTING TO DSL
----------------------------------------------------------------------
[OK] Natural Language Parser

Entry Rule: ENTRY: CLOSE GT SMA(CLOSE, 30) AND VOLUME GT 1000000
Exit Rule:  EXIT: CLOSE LT SMA(CLOSE, 20)

----------------------------------------------------------------------
STEP 2: PARSING DSL
----------------------------------------------------------------------
[OK] DSL Parser (Lark Grammar)
Abstract Syntax Tree built successfully

... (more steps)

======================================================================
BACKTEST RESULTS
======================================================================

Total Return:            0.00%
Max Drawdown:            0.00%
Number of Trades:           0

======================================================================
STRATEGY EXECUTION SUCCESSFUL!
======================================================================
```

---

## 📝 Writing Strategies

### Basic Format

**Entry condition:**
```
"Buy when [condition]"
"Enter when [condition]"
```

**Exit condition:**
```
"Sell when [condition]"
"Exit when [condition]"
```

### Real Examples

**Example 1: Simple Moving Average**
```
Buy when close is above 20-day moving average.
Sell when close drops below 50-day moving average.
```

**Example 2: With Volume Filter**
```
Buy when close is above 20-day moving average and volume is above 1 million.
Sell when close drops below 50-day moving average.
```

**Example 3: Multiple Conditions**
```
Enter when close is above 30-day moving average and volume is above 2 million.
Exit when close falls below 20-day moving average or volume drops below 500000.
```

**Example 4: RSI Based**
```
Buy when RSI(14) is above 70.
Sell when RSI(14) drops below 30.
```

---

## 🎯 What Each Menu Option Does

### Option 1: Enter Your Strategy
- You type your strategy in plain English
- System converts it to DSL
- Parses it to AST
- Generates Python code
- Executes it
- Shows backtest results

### Option 2: See Example Strategies
Shows 3 working examples:
1. **Moving Average** - Classic crossover strategy
2. **Breakout** - Entry on breakout, exit on reversal
3. **Volume Breakout** - Combines price and volume

### Option 3: See Supported Phrases
Shows all the English phrases you can use:
- Price fields: close, volume, high, low, open
- Operators: above, below, greater than, less than
- Indicators: 20-day moving average, RSI(14)
- Logic: and, or
- Numbers: 1 million, 2 million, 500000

### Option 4: Exit
Closes the program

---

## 🚀 Quick Test Mode

### Run Directly from Command Line

```bash
# One-liner test
python interactive_strategy.py "Buy when close is above 50-day moving average. Sell when close drops below 20-day moving average."
```

**Output:**
```
======================================================================
QUICK TEST MODE
======================================================================

Strategy: Buy when close is above 50-day moving average...

----------------------------------------------------------------------
STEP 1: CONVERTING TO DSL
----------------------------------------------------------------------
[OK] Natural Language Parser
Entry Rule: ENTRY: CLOSE GT SMA(CLOSE, 50)
Exit Rule:  EXIT: CLOSE LT SMA(CLOSE, 20)

... (continues with all steps)

======================================================================
BACKTEST RESULTS
======================================================================

Total Return:            X.XX%
Max Drawdown:            X.XX%
Number of Trades:           X

======================================================================
STRATEGY EXECUTION SUCCESSFUL!
======================================================================
```

---

## 💡 Step-by-Step Execution

The system shows you each step:

```
STEP 1: CONVERTING TO DSL
[OK] Natural Language Parser
Shows your English converted to DSL syntax

STEP 2: PARSING DSL
[OK] DSL Parser (Lark Grammar)
Shows that the DSL was parsed successfully

STEP 3: GENERATING PYTHON CODE
[OK] Code Generator
Shows how many lines of Python code were generated

STEP 4: LOADING DATA
[OK] Data Loader
Shows date range and columns of price data

STEP 5: EXECUTING STRATEGY
[OK] Strategy Execution
Shows that signals were generated successfully

STEP 6: BACKTESTING
[OK] Backtest Complete
Shows backtest results (return %, drawdown %, trades)
```

---

## ✅ Supported Phrases Reference

### Price Fields
```
close price, close, volume, high, low, open
```

### Comparison Operators
```
above, below, greater than, less than, equal to
```

### Indicators
```
20-day moving average
50 day moving average
RSI(14)
RSI(21)
```

### Logic
```
and, or (can combine multiple conditions with parentheses)
```

### Numbers
```
1 million, 2 million, 500000, 1000000, etc.
```

### Entry/Exit Keywords
```
buy, enter, sell, exit, when
```

---

## 🎮 Try These Strategies

### Strategy 1: Basic Moving Average
```
Buy when close is above 20-day moving average.
Sell when close drops below 50-day moving average.
```

### Strategy 2: Volume + Price
```
Buy when close is above 30-day moving average and volume is above 1 million.
Sell when close drops below 30-day moving average.
```

### Strategy 3: Multiple Entry Conditions
```
Enter when close is above 50-day moving average and volume is above 2 million.
Exit when close falls below 20-day moving average.
```

### Strategy 4: Breakout
```
Enter when close is above 60-day moving average.
Exit when close falls below 30-day moving average.
```

### Strategy 5: Simple Reversal
```
Buy when close is above 20-day moving average.
Sell when close is below 10-day moving average.
```

---

## 🔍 Understanding the Output

### DSL Output
```
Entry Rule: ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000
Exit Rule:  EXIT: CLOSE LT SMA(CLOSE, 50)
```

This is the machine-readable format of your strategy.

### Generated Code Sample
```python
from pandas import DataFrame
from engine.data_utils import calculate_sma

def calculate_signals(df: DataFrame) -> DataFrame:
    sma_20 = calculate_sma(df['CLOSE'], 20)
    sma_50 = calculate_sma(df['CLOSE'], 50)
    
    entry_signals = (df['CLOSE'] > sma_20) & (df['VOLUME'] > 1000000)
    exit_signals = df['CLOSE'] < sma_50
    
    return signals
```

This is the actual Python code that will be executed.

### Backtest Results
```
Total Return:      X.XX%
Max Drawdown:      X.XX%
Number of Trades:     X
```

- **Total Return:** Profit/loss percentage
- **Max Drawdown:** Largest peak-to-trough decline
- **Number of Trades:** How many entry/exit pairs occurred

---

## 🚀 Next Steps

1. **Try it:** `python interactive_strategy.py`
2. **Pick a strategy:** Enter your own English description
3. **See results:** Watch each step execute
4. **Iterate:** Try different conditions and indicators
5. **Learn:** Check the supported phrases section

---

## 📝 Tips

✅ **Do:**
- Be specific: "20-day moving average" not "average"
- Use clear comparisons: "above" or "below"
- Combine with "and" or "or"
- Mention both entry and exit conditions

❌ **Don't:**
- Use vague terms: "good" or "high volume"
- Use unsupported indicators
- Forget entry or exit condition
- Use technical jargon not in the supported list

---

## 🎯 Common Mistakes

**Mistake:** `"Buy when price goes up"`
**Why:** "goes up" is not supported
**Fix:** `"Buy when close is above 20-day moving average"`

**Mistake:** `"Buy when RSI is high"`
**Why:** "high" is not specific
**Fix:** `"Buy when RSI(14) is above 70"`

**Mistake:** `"Buy and hold forever"`
**Why:** No exit condition
**Fix:** Add an exit condition like `"Sell when close drops below 50-day moving average"`

---

## 🎉 You're Ready!

Just run:
```bash
python interactive_strategy.py
```

And start typing your trading strategies! 🚀
