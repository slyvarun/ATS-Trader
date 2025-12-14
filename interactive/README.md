# 🎮 Interactive Strategy Builder

**Type your trading strategies in English and watch them execute instantly!**

## Quick Start

```bash
python interactive_strategy.py
```

This opens an interactive menu where you can:
1. **Enter your strategy** - Type in plain English
2. **See examples** - Learn from 3 working strategies
3. **See supported phrases** - Reference for what you can say
4. **Exit** - Close the program

## Alternative: Quick Test

Run directly with your strategy:
```bash
python interactive_strategy.py "Buy when close is above 20-day moving average. Sell when close drops below 50-day moving average."
```

## Files in This Folder

- **interactive_strategy.py** - Main interactive script
- **INTERACTIVE_QUICK_START.md** - 2-minute quick reference
- **INTERACTIVE_GUIDE.md** - Detailed guide with all options
- **INTERACTIVE_COMPLETE.md** - Complete documentation
- **README_INTERACTIVE.md** - Feature overview

## Example Strategy

```
Buy when close is above 20-day moving average and volume is above 1 million.
Sell when close drops below 50-day moving average.
```

The system automatically:
1. Converts English to DSL
2. Parses to Abstract Syntax Tree
3. Generates Python code
4. Executes on historical data
5. Shows backtest results

## Supported Phrases

- **Prices:** close, volume, high, low, open
- **Operators:** above, below, greater than, less than, equal to
- **Indicators:** 20-day moving average, RSI(14)
- **Logic:** and, or
- **Entry/Exit:** buy/enter when, sell/exit when

## How It Works

```
Your English
    ↓
Natural Language Parser
    ↓
DSL (Domain Specific Language)
    ↓
DSL Parser (Lark)
    ↓
Abstract Syntax Tree
    ↓
Python Code Generator
    ↓
Execution & Backtest
    ↓
Results
```

All automatically! ✨

## Try It Now

```bash
python interactive_strategy.py
```

Then choose option 1, type a strategy, and watch it execute! 🚀
