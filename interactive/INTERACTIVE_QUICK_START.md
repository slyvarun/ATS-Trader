# ✨ Interactive Strategy Builder - Quick Start

## 🎮 How to Use (2 Ways)

### Way 1: Interactive Menu (Recommended)

```bash
python interactive_strategy.py
```

Then choose:
1. Enter your strategy
2. See examples
3. See supported phrases
4. Exit

### Way 2: Quick Test (One-Liner)

```bash
python interactive_strategy.py "Buy when close is above 20-day moving average. Sell when close drops below 50-day moving average."
```

---

## 📝 How to Write a Strategy

Just describe it in English:

```
"Buy when close is above 20-day moving average and volume is above 1 million.
 Sell when close drops below 50-day moving average."
```

**That's it!** The system handles everything else.

---

## 🎯 Example Strategies to Try

### 1. Simple Moving Average
```
Buy when close is above 20-day moving average.
Sell when close drops below 50-day moving average.
```

### 2. With Volume
```
Buy when close is above 30-day moving average and volume is above 1 million.
Sell when close drops below 30-day moving average.
```

### 3. Breakout Strategy
```
Enter when close is above 60-day moving average.
Exit when close falls below 30-day moving average.
```

### 4. RSI Based
```
Buy when RSI(14) is above 70.
Sell when RSI(14) drops below 30.
```

---

## 📖 Supported Phrases

| Category | Examples |
|----------|----------|
| **Prices** | close price, volume, high, low, open |
| **Operators** | above, below, greater than, less than, equal to |
| **Indicators** | 20-day moving average, RSI(14) |
| **Logic** | and, or |
| **Numbers** | 1 million, 2 million, 500000 |
| **Entry/Exit** | buy/enter when, sell/exit when |

---

## 🚀 Complete Example

**Your command:**
```bash
python interactive_strategy.py
```

**System shows menu:**
```
1. Enter your strategy
2. See example strategies
3. See supported phrases
4. Exit

Choose option (1-4): 1
```

**You type `1`**

**System asks for strategy:**
```
Start typing (press Enter twice when done):
```

**You type:**
```
Buy when close is above 20-day moving average.
Sell when close drops below 50-day moving average.

```

**System processes and shows:**
```
STEP 1: CONVERTING TO DSL
Entry Rule: ENTRY: CLOSE GT SMA(CLOSE, 20)
Exit Rule:  EXIT: CLOSE LT SMA(CLOSE, 50)

STEP 2: PARSING DSL
[OK] DSL Parser successful

STEP 3: GENERATING PYTHON CODE
[OK] Generated 754 lines of code

STEP 4: LOADING DATA
[OK] Loaded 25 rows of price data

STEP 5: EXECUTING STRATEGY
[OK] Signals generated successfully

STEP 6: BACKTESTING
[OK] Backtest Complete

BACKTEST RESULTS
Total Return:      0.00%
Max Drawdown:      0.00%
Number of Trades:     0

STRATEGY EXECUTION SUCCESSFUL!
```

---

## 💡 What Happens Behind The Scenes

```
Your English
    ↓
Natural Language Parser
    ↓
Domain Specific Language (DSL)
    ↓
DSL Parser (Lark)
    ↓
Abstract Syntax Tree (AST)
    ↓
Python Code Generator
    ↓
Python Code Execution
    ↓
Backtest Results
```

All automatically! ✨

---

## 🎓 Menu Options

### Option 1: Enter Your Strategy
- Type your strategy
- See all 6 execution steps
- Get backtest results
- Return to menu

### Option 2: See Examples
- View 3 sample strategies
- See exactly how they're written
- Return to menu

### Option 3: See Supported Phrases
- Learn what you can say
- Get comprehensive list
- Return to menu

### Option 4: Exit
- Close the program
- Save your work first!

---

## ✅ What You Get

For each strategy:

1. **DSL Conversion** - See English converted to machine format
2. **Parsing Confirmation** - Verify the syntax is correct
3. **Generated Code** - See actual Python that will run
4. **Data Loaded** - Confirmation of test data
5. **Execution Status** - Signals generated successfully
6. **Backtest Results** - Return %, Drawdown %, Trade count

---

## 🚀 Try It Now!

```bash
python interactive_strategy.py
```

Then:
1. Choose option 1
2. Type a strategy
3. Press Enter twice
4. Watch it execute!

---

## 📚 More Information

- **INTERACTIVE_GUIDE.md** - Full detailed guide
- **HOW_TO_USE_CUSTOM_STRATEGIES.md** - Strategy writing tips
- **START_HERE.md** - Project overview
- **ANSWER_USER_INPUT.md** - How the system works

---

## 💻 Two Ways to Run

**Interactive (Recommended for Beginners):**
```bash
python interactive_strategy.py
# Then follow the menu
```

**Quick Test (Advanced Users):**
```bash
python interactive_strategy.py "Your strategy here"
# Runs immediately without menu
```

---

**That's it! Start typing your trading strategies now! 🎉**
