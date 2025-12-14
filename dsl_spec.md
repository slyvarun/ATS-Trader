# ATS Trader DSL - The Robot's Language 🤖📊# ATS Trader DSL - The Robot's Language 🤖📊



Alright, so this file is basically the instruction manual for how to talk to the robot. It's like grammar rules, but instead of "nouns and verbs," it's "prices and indicators."Think of this like the grammar rules for the robot! Just like English has rules (nouns, verbs, adjectives), the robot's special trading language has rules too.



## What's a Strategy Anyway?## What is a Strategy? 



A strategy is just a plan with two parts:A strategy is a plan with TWO parts:



1. **ENTRY** - When you want to BUY 💰1. **ENTRY** - When to BUY 💰

2. **EXIT** - When you want to SELL 💵2. **EXIT** - When to SELL 💵



That's it. You gotta tell the robot both. You can't just have one without the other, or the robot gets confused.**Simple Example:**

```

## The Basic Rules of Robot LanguageENTRY: Buy when price is high

EXIT: Sell when price is low

### What Can You Check? (The Prices)```



| Name | What It Actually Means |## 🎯 The Robot's Language Rules

|------|---|

| `CLOSE` | The price when the market closes for the day |### What Can You Check? (The Prices)

| `OPEN` | The price when the market opens in the morning |

| `HIGH` | The highest price that whole day || Name | What It Means |

| `LOW` | The lowest price that whole day ||------|-------------|

| `VOLUME` | How many shares people traded that day || `CLOSE` | The price at the end of the day |

| `OPEN` | The price at the start of the day |

So if I say `CLOSE GT 100`, I'm saying "Is the closing price greater than 100?"| `HIGH` | The highest price that day |

| `LOW` | The lowest price that day |

### What Can You Compare? (The Operators)| `VOLUME` | How many shares people traded |



These are the words you use to compare stuff:**Example:** `CLOSE GT 100` means "Price at end of day > 100"



| Robot Says | What It Means | Example |### What Can You Compare? (The Operators)

|-----------|---|---------|

| `GT` | Greater Than (>) | `CLOSE GT 100` = price > 100 || Robot Word | Real Meaning | Example |

| `LT` | Less Than (<) | `CLOSE LT 50` = price < 50 ||-----------|---|---------|

| `GTE` | Greater or Equal (>=) | `CLOSE GTE 100` = price >= 100 || `GT` | Greater Than (>) | `CLOSE GT 100` means price > 100 |

| `LTE` | Less or Equal (<=) | `CLOSE LTE 50` = price <= 50 || `LT` | Less Than (<) | `CLOSE LT 50` means price < 50 |

| `EQ` | Equals (==) | `CLOSE EQ 100` = price = 100 || `GTE` | Greater or Equal (>=) | `CLOSE GTE 100` means price >= 100 |

| `NEQ` | Not Equal (!=) | `CLOSE NEQ 100` = price ≠ 100 || `LTE` | Less or Equal (<=) | `CLOSE LTE 50` means price <= 50 |

| `EQ` | Equals (==) | `CLOSE EQ 100` means price = 100 |

Pretty straightforward, right?| `NEQ` | Not Equal (!=) | `CLOSE NEQ 100` means price ≠ 100 |



### How Do You Put Rules Together? (AND & OR)### How Do You Combine Rules? (AND & OR)



This is where it gets interesting:Like in English:

- **AND** = BOTH things must be true

- **AND** = Both things must be true- **OR** = At least ONE thing must be true

- **OR** = At least one thing must be true

**Examples:**

So like:```

CLOSE GT 100 AND VOLUME GT 1000000

```Meaning: Price > 100 AND lots of people are trading

CLOSE GT 100 AND VOLUME GT 1000000

= Price > 100 AND lots of people tradingCLOSE GT 100 OR VOLUME GT 1000000  

Meaning: Either price > 100 OR lots of people are trading (or both)

CLOSE GT 100 OR VOLUME GT 1000000```

= Either price > 100 OR lots of people trading (or both)

```## 🧮 Special Tricks - Technical Indicators



You can string together as many of these as you want.### SMA (Simple Moving Average)

**What does it do?** Calculates the average price over the last N days

## The Fancy Tricks - Technical Indicators

**Why use it?** Smooths out daily jumps to show the real trend

### Simple Moving Average (SMA)

**Example:**

Okay, so SMA is just the average price over the last N days. It smooths out all the daily ups and downs and shows you the real trend.```

SMA(CLOSE, 20)

```= Average of the last 20 days' closing prices

SMA(CLOSE, 20)

= Average of the last 20 days' closing pricesIf today's price is above this average, the trend might be UP! 📈

If today's price is below this average, the trend might be DOWN! 📉

If today's price is above this, trend is up.```

If today's price is below this, trend is down.

```### RSI (Relative Strength Index)

**What does it do?** Measures if a stock is too popular or unpopular (0-100 scale)

### Relative Strength Index (RSI)

**Why use it?** Tells you if a stock will go up or down soon

RSI tells you how much momentum a stock has. It's on a scale from 0 to 100. You read it like this:

**How to read it:**

```- `RSI > 70` = TOO POPULAR (people are buying too much, might fall soon) ⚠️

RSI(CLOSE, 14)- `RSI < 30` = UNPOPULAR (people avoid it, might go up soon) 📈

= How strong is the stock based on the last 14 days?- `RSI = 50` = Just right! 👍



RSI > 70 = Stock is TOO popular, might fall soon (dangerous!)**Example:**

RSI < 30 = Stock is UNPOPULAR, might go up soon (opportunity!)```

RSI = 50 = Normal, nothing special going onRSI(CLOSE, 14)

```= Strength based on last 14 days of prices

```

Basically, it's like a momentum meter.

## 📝 Real Examples - Learn by Doing!

## Real Examples - Let's See Some Actual Strategies

### Example 1: "Buy High, Sell Higher" 📈

### Example 1: Simple SMA Crossover```

ENTRY: CLOSE GT SMA(CLOSE, 20)

```EXIT: CLOSE LT SMA(CLOSE, 20)

ENTRY: CLOSE GT SMA(CLOSE, 20)```

EXIT: CLOSE LT SMA(CLOSE, 20)**What it means:** 

```- Buy when price > 20-day average (uptrend!)

- Sell when price < 20-day average (downtrend!)

What this means: Buy when price is above its 20-day average (uptrend!), sell when price drops below it (downtrend!). This is a classic strategy that a lot of people use.

### Example 2: "Volume Matters!" 📊

### Example 2: SMA + Volume Filter```

ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000

```EXIT: CLOSE LT SMA(CLOSE, 50)

ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000```

EXIT: CLOSE LT SMA(CLOSE, 50)**What it means:**

```- Buy when price > 20-day average AND lots of people trading

- Sell when price < 50-day average (big fall!)

What this means: Only buy if BOTH conditions are true - price above 20-day average AND lots of people trading. Sell when price drops below 50-day average. This one is more strict because it requires high volume.

### Example 3: "Find the Weak Ones" 💪

### Example 3: RSI Overbought/Oversold```

ENTRY: RSI(CLOSE, 14) LT 30

```EXIT: RSI(CLOSE, 14) GT 70

ENTRY: RSI(CLOSE, 14) LT 30```

EXIT: RSI(CLOSE, 14) GT 70**What it means:**

```- Buy when RSI < 30 (stock is weak, will bounce back!)

- Sell when RSI > 70 (stock is too strong, will fall!)

What this means: Buy when RSI is low (stock is weak, will bounce), sell when RSI is high (stock is too strong, will fall). This is betting on mean reversion - things tend to go back to normal.

### Example 4: "Multiple Choices" 🤔

### Example 4: Multiple Options```

ENTRY: (CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000) OR RSI(CLOSE, 14) LT 30

```EXIT: CLOSE LT SMA(CLOSE, 50) OR RSI(CLOSE, 14) GT 80

ENTRY: (CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000) OR RSI(CLOSE, 14) LT 30```

EXIT: CLOSE LT SMA(CLOSE, 50) OR RSI(CLOSE, 14) GT 80**What it means:**

```- Buy if (price up AND volume high) OR (stock is weak)

- Sell if (price below 50-day) OR (stock too strong)

What this means: Buy if EITHER (price up AND volume high) OR (RSI is low). Sell if EITHER (price below 50-day) OR (RSI is too high). This one gives you more flexibility.

## ✅ Rules the Robot Follows

## The Rules You Gotta Follow

1. **You MUST have ENTRY and EXIT** - The robot needs to know when to buy AND sell

If you don't follow these, the robot gets mad:2. **Numbers must be positive** - Can't have negative prices!

3. **Field names are CLOSE, OPEN, HIGH, LOW, VOLUME** - No other names work!

1. **You MUST have both ENTRY and EXIT** - The robot needs to know when to buy AND sell. Can't have just one.4. **Indicators are SMA and RSI** - Can't make up your own indicators (yet!)

5. **You can use AND/OR to combine rules** - Mix and match as much as you want!

2. **Use only the price names we support** - CLOSE, OPEN, HIGH, LOW, VOLUME. Nothing else. No made-up names.

## 🐛 If Something Goes Wrong...

3. **Numbers must be positive** - You can't have negative prices. That doesn't make sense.

### Error: "Unknown field: PRICE"

4. **Indicators are SMA and RSI only (for now)** - Can't make up your own indicators yet. Just these two.**Why:** The robot doesn't know what "PRICE" is

**Fix:** Use CLOSE instead

5. **Use AND/OR to combine multiple rules** - You can be as creative as you want with combinations.

### Error: "Unknown indicator: EMA"  

6. **Parentheses must be balanced** - Every opening `(` needs a closing `)`. Simple but easy to mess up.**Why:** The robot only knows SMA and RSI

**Fix:** Use SMA(CLOSE, 20) instead

## If Something Goes Wrong...

### Error: "Missing closing parenthesis"

Sometimes the robot gets confused. Here are the common errors:**Why:** You forgot to close your brackets

**Fix:** Make sure every `(` has a `)`

### Error: "Unknown field: PRICE"

**Why**: You made up a field name that doesn't exist---

**How to fix**: Use one of the real ones: CLOSE, OPEN, HIGH, LOW, VOLUME

**Status**: ✅ DSL Rules Complete!

### Error: "Unknown indicator: EMA"**Version**: 1.0

**Why**: You tried to use an indicator we don't support yet**Easy to Read?**: YES! 👍
**How to fix**: Use SMA or RSI instead

### Error: "Missing closing parenthesis"
**Why**: You forgot to close your brackets
**How to fix**: Count your `(` and make sure they all have `)` partners

### Error: "Expected ENTRY/EXIT"
**Why**: You didn't write ENTRY or EXIT at the beginning
**How to fix**: Always start with `ENTRY:` and end with `EXIT:`

## How the Robot Actually Reads This

When you write something like:

```
ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000
```

The robot breaks it down into pieces:

```
{
  "type": "binary_op",      ← It's an AND operation
  "op": "AND",
  "left": {                 ← First part
    "type": "comparison",
    "op": "GT",
    "left": "CLOSE",        ← The closing price
    "right": "SMA(CLOSE, 20)" ← The 20-day average
  },
  "right": {                ← Second part
    "type": "comparison",
    "op": "GT",
    "left": "VOLUME",       ← The volume
    "right": "1000000"      ← The number
  }
}
```

Don't worry about that fancy stuff though - the robot handles it all automatically. You just need to write the English-ish version, and it figures out the rest.

## Tips for Writing Good Strategies

Here's what I've learned from using this thing:

1. **Keep it simple first** - Start with one condition, make sure it works, then add more.

2. **Volume is important** - Lots of successful strategies filter by volume. It shows people actually care about the stock.

3. **Combine multiple indicators** - Don't rely on just one thing. Use SMA + RSI together for better results.

4. **Test with old prices** - The robot does this automatically. Check if your strategy would've worked in the past.

5. **Use both moving averages** - 20-day is fast, 50-day is slow. Together they're powerful.

6. **Think about timeframes** - What works on daily might not work on weekly. You gotta think about what you're doing.

## Examples of BAD Strategies (Don't Do These)

```
← Wrong: Comparing two prices
ENTRY: CLOSE GT OPEN

← Wrong: RSI = 50 (almost never happens exactly)
ENTRY: RSI(CLOSE, 14) EQ 50

← Wrong: Only uses one indicator, too simple
ENTRY: CLOSE GT 100
```

## Examples of GOOD Strategies

```
← Good: Combines trend + volume
ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000

← Good: Multiple conditions for confirmation
ENTRY: (CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000) OR RSI(CLOSE, 14) LT 30

← Good: Clear risk management
EXIT: CLOSE LT SMA(CLOSE, 50)
```

## What's Coming in the Future?

I'm planning to add:

- More indicators (MACD, Bollinger Bands, etc.)
- Time-based rules ("only between 9am-11am")
- Risk management ("stop loss at -2%")
- Custom indicators you can define yourself

But for now, this is what we've got. It's pretty powerful though!

## Final Thoughts

That's basically the whole language. It's not super complicated - just prices, comparisons, and logic. You can build some pretty sophisticated strategies with just these pieces.

The key is to think about what you're doing. Don't just throw random rules together. Think about WHY each rule is there. What behavior are you trying to capture?

Good luck building your strategies!

---

**Status**: This is the current language spec. It works and is stable!

**Last Updated**: December 9, 2025
