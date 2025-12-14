# ATS-Trader: The Robot Trader! 🤖📈# ATS-Trader: The Robot Trader! 🤖📈



So hey, I built this thing called ATS-Trader. Basically, I got tired of having to code up trading strategies every time I had a new idea. Like, why should I have to write pages of Python code just to test if my theory works? That's where this project came in.So hey, I built this thing called ATS-Trader. Basically, I got tired of having to code up trading strategies every time I had a new idea. Like, why should I have to write pages of Python code just to test if my theory works? That's where this project came in.



Here's the idea: I wanted to be able to just talk about my trading ideas in plain English, and have the computer understand what I meant and actually run it. So instead of writing code, I can just say something like "Buy when the price goes up, sell when it goes down" and the robot will figure out the rest.Here's the idea: I wanted to be able to just talk about my trading ideas in plain English, and have the computer understand what I meant and actually run it. So instead of writing code, I can just say something like "Buy when the price goes up, sell when it goes down" and the robot will figure out the rest.



Pretty cool, right? Let me walk you through what it does.Pretty cool, right? Let me walk you through what it does.



## What Actually Happens Here?## What Actually Happens Here?



Okay, so the whole thing works in 5 steps:Okay, so the whole thing works in 5 steps:



1. **You tell it what to do** - You just describe your trading strategy in normal English. Like, literally just tell it what you want.1. **You tell it what to do** - You just describe your trading strategy in normal English. Like, literally just tell it what you want.

2. **It translates your words** - The computer converts what you said into a special language that it understands better.2. **It translates your words** - The computer converts what you said into a special language that it understands better.

3. **It makes a game plan** - It breaks down your strategy into step-by-step instructions, kind of like a recipe.3. **It makes a game plan** - It breaks down your strategy into step-by-step instructions, kind of like a recipe.

4. **It writes the actual code** - Then it automatically generates Python code that does exactly what you want.4. **It writes the actual code** - Then it automatically generates Python code that does exactly what you want.

5. **It tests everything** - Finally, it runs your strategy on old stock prices to see if it would've actually made money.5. **It tests everything** - Finally, it runs your strategy on old stock prices to see if it would've actually made money.



## How Does It Actually Work? (The Technical Part)## 🧠 How Does It Work? (Step by Step)



Alright, so the process is pretty straightforward. Let me show you:Think of it like cooking! 👨‍🍳



``````

STEP 1: You talk in EnglishSTEP 1: You talk (English)

   "I wanna buy when the price is above the 20-day average   "Buy when price is high and lots of people are selling"

   and a ton of people are trading"   ↓

   ↓STEP 2: Computer understands (DSL - Special Trading Language)

STEP 2: Computer translates it to special language   "ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000"

   "ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000"   ↓

   ↓STEP 3: Make a plan (AST - Like a recipe ingredients list)

STEP 3: Creates an instruction list (like a plan)   {Binary operation: AND

   {It's an AND operation with two checks:     - First part: CLOSE > 20-day average

     - First: Is CLOSE > 20-day average?     - Second part: VOLUME > 1 million}

     - Second: Is VOLUME > 1 million?}   ↓

   ↓STEP 4: Write the code (Python - What the computer runs)

STEP 4: Writes the Python code   if (price > average) AND (volume > 1000000):

   if (price > average) AND (trades > 1000000):      BUY!

      BUY!   ↓

   ↓STEP 5: Test it (Did it work with old prices?)

STEP 5: Tests it with real old prices   "If you used this strategy last year, you would have made $1000!"

   "Hey, if you used this last year, you'd have made $1000!"```

```

## 🚀 Let's Try It!

## Alright, Let's Get It Running

### Install the Robot

### First, Install Everything You Need```bash

pip install -r requirements.txt

```bash```

pip install -r requirements.txt

```### Run the Demo

```bash

This grabs all the packages you need. Nothing fancy here.python test.py

```

### Then Run the Demo

You'll see:

```bash1. The robot listening to an example trading idea ✅

python test.py2. The robot converting it to computer language ✅

```3. The robot testing it with real stock prices ✅

4. Results: "This strategy would have made $XXX!" ✅

When you run this, you'll see:

### Real Example: The "Buy Low, Sell High" Strategy 💰

1. Your strategy idea in English ✓

2. How the robot translated it ✓**What you say:**

3. The breakdown of how it's gonna work ✓```

4. Your trading signals getting generated ✓Buy when the price is above the 20-day average 

5. Some results showing if it would've worked ✓AND people are trading a lot (volume > 1 million)

Exit when price drops below 50-day average

## Real Example: What I Actually Use```



Let me give you a real strategy that I like. Here's the English version:**Robot's computer language:**

```

```ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000

"I want to buy when the close price is above the 20-day average EXIT: CLOSE LT SMA(CLOSE, 50)

AND when there's a lot of volume (meaning people are actually ```

interested in trading). Then I'll sell when the price drops below 

the 50-day average because that's a sign things are going downhill."**Robot's step-by-step plan:**

``````

Step 1: Get the closing price

Here's what the robot language looks like:Step 2: Calculate the 20-day average price

Step 3: Check if price > 20-day average

```Step 4: Check if trading volume > 1 million

ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000Step 5: If BOTH are true, BUY!

EXIT: CLOSE LT SMA(CLOSE, 50)Step 6: When price drops below 50-day average, SELL!

``````



And here's the Python code it generates:**Robot writes code that does this automatically!** 🤖



```python## 📁 Files Inside the Robot

def calculate_signals(df):

    signals = DataFrame(index=df.index, data={'entry': nan, 'exit': nan})```

    signals['entry'] = ((df['CLOSE'] > calculate_sma(df['CLOSE'], 20)) ATS-Trader/

                        & (df['VOLUME'] > 1000000.0))├── engine/

    signals['exit'] = (df['CLOSE'] < calculate_sma(df['CLOSE'], 50))│   ├── nl_parser.py         ← Listens to your English words

    return signals.fillna(False)│   ├── dsl_parser.py        ← Translates to robot language

```│   ├── code_generator.py    ← Writes the computer code

│   ├── backtester.py        ← Tests with old prices

Pretty neat, huh? The robot just wrote all that for me.│   └── data_utils.py        ← Gets the stock prices

├── test.py                  ← Run this to test everything!

## Inside the Box - What Files Are There?├── dsl_spec.md              ← Robot language rules (like grammar)

└── requirements.txt         ← Things the robot needs

``````

ATS-Trader/

├── engine/## 🔧 The 4 Brain Parts of the Robot 🧠

│   ├── nl_parser.py         → Listens to your English

│   ├── dsl_parser.py        → Translates to robot language### 1. **The Ear** (`nl_parser.py`) 👂

│   ├── code_generator.py    → Writes the actual codeThis part LISTENS to what you say in English and understands it.

│   ├── backtester.py        → Tests with old prices- You: "Buy when price goes above average"

│   └── data_utils.py        → Handles the stock prices- Ear hears: ✓

├── test.py                  → Run this to try everything!

├── dsl_spec.md              → Rules of the robot language### 2. **The Translator** (`dsl_parser.py`) 🗣️

└── requirements.txt         → What you need to installThis part translates English into Special Robot Language.

```- English: "CLOSE GT SMA(CLOSE, 20)"

- Robot Language: Same thing, but in a way the computer understands!

## The 4 Main Parts

### 3. **The Coder** (`code_generator.py`) 💻

### The Ear (nl_parser.py)This part writes actual computer code based on the robot language.

This part just listens to what you say in English and makes sure it understands. It's basically reading your words and figuring out what they mean. If you say "buy when price is high," it needs to convert that into something the computer can understand.- Robot Language: `CLOSE GT 100 AND VOLUME GT 1000000`

- Computer Code: `if (price > 100) AND (trades > 1000000): BUY`

### The Translator (dsl_parser.py)

This takes what you said and converts it to the robot's special trading language. Think of it like translating English to Spanish, except it's English to "Robot Trading Language." It's a specific format that the computer understands really well.### 4. **The Tester** (`backtester.py`) 🧪

This part tests the strategy with OLD prices to see if it would have worked.

### The Coder (code_generator.py)- "If you used this 10 years ago, you would have made $5,000!"

Once the robot understands your idea, this part writes actual Python code that will execute your strategy. It's basically writing the program that will do the trading. This is where the magic happens - it goes from "robot language" to real, runnable code.

## 📈 What Prices Can You Check? 📊

### The Tester (backtester.py)

This is the cool part - it takes your new strategy and tests it with prices from the past. So you can see "Hey, if I had done this a year ago, would I have made money?" It's like simulating your strategy in a video game before you use real money.You can tell the robot to look at:

- **CLOSE** - The ending price of the day

## What Prices Can You Use?- **OPEN** - The starting price of the day  

- **HIGH** - The highest price that day

You've got access to:- **LOW** - The lowest price that day

- **CLOSE** - The price at the end of the day- **VOLUME** - How many people traded

- **OPEN** - The price at the beginning of the day

- **HIGH** - The highest price that day## 🎯 What Special Tricks Can You Do?

- **LOW** - The lowest price that day

- **VOLUME** - How many people traded### Moving Average (SMA)

"Average price over the last 20 days"

You can use any of these in your strategy. Honestly, I use CLOSE and VOLUME most of the time.```

Example: SMA(CLOSE, 20)

## The Cool Tricks You Can DoMeaning: What was the average price for the last 20 days?

```

### Moving Average (SMA)

This is basically the average price over the last N days. It smooths out the daily noise and shows you the real trend. If today's price is above this, the trend is probably up. If it's below, the trend is probably down.### Strength Index (RSI)

"How strong/weak is the stock on a scale of 0-100"

``````

SMA(CLOSE, 20)Example: RSI(CLOSE, 14)  

= What was the average closing price over the last 20 days?If RSI > 70 = Stock is too popular, might fall (⬇️)

```If RSI < 30 = Stock is unpopular, might go up (⬆️)

If RSI = 50 = Normal

### Relative Strength Index (RSI)```

This tells you if a stock is being bought too much or ignored too much. It's on a scale from 0 to 100.

## 🐛 We Fixed 3 Big Problems! ✅

```

RSI(CLOSE, 14)### Problem 1: Robot Couldn't Understand AND/OR 🤔

**What happened:** When you said "AND", the robot didn't know what to do!

If RSI > 70 = Everyone's buying it, might fall soon**What we did:** Taught the robot to understand AND/OR logic! ✓

If RSI < 30 = Nobody wants it, might go up soon

If RSI = 50 = Pretty normal, nothing special### Problem 2: Column Names Were Broken 😫  

```**What happened:** The robot looked for `'CLOSE'` but found `' CLOSE'` (with space)

**What we did:** Remove the spaces! ✓

## Bugs We Fixed

### Problem 3: Missing Important Parts 🧩

Yeah, we ran into some issues during development. Here's what we dealt with:**What happened:** Some important functions weren't there

**What we did:** Added all the missing pieces! ✓

### The AND/OR Problem

At first, the robot didn't understand how to handle AND/OR logic. It would get confused when you said "buy when this AND that." We fixed it by teaching the robot how to understand logical operations properly.## 📋 How to Use It (Easy Steps!)



### The Column Name Problem### Step 1: Tell the Robot What to Do (English)

There was this weird issue where the robot was looking for a column called 'CLOSE' but it was actually called ' CLOSE' with a space at the beginning. Simple fix but took forever to track down! Just had to strip the whitespace.```

"Buy when close price is above the 20-day average AND volume is above 1 million"

### Missing Pieces```

Some functions weren't hooked up properly. We added all the missing parts so everything connects correctly now. Everything works together as expected.

### Step 2: Run the Test

## How to Test It```bash

python test.py

Run the main test:```

```bash

python test.py### Step 3: Watch the Magic! ✨

```The robot will:

1. Listen to your words ✓

You'll see it working through all the steps and outputting results at the end.2. Translate to special robot language ✓

3. Write computer code ✓

Want to see what code it actually generated?4. Test with real stock prices ✓

```bash5. Tell you: "This would have made money!" or "This would have lost money!" ✓

python debug_codegen.py

```## 🧪 Testing the Robot



Want to see the prices it's working with?### Run the Main Test

```bash```bash

python debug_data.pypython test.py

``````



These debug scripts are super helpful if something doesn't seem right.**What you'll see:**

```

## What You Need to Install[1] You said: "Buy when the close price is above..."

[2] Robot translated: "ENTRY: CLOSE GT SMA(CLOSE, 20) AND VOLUME GT 1000000"

Just three things:[3] Robot made a plan (AST)

- **Lark** - Helps the robot understand languages[4] Robot wrote the code

- **Pandas** - For handling and reading the data[5] Signals Generated Successfully!

- **NumPy** - For doing all the math stuff[6] Results: "Total Return: 5.2%"

```

Just run this once:

```bash### Debug Tools (For curious people!)

pip install -r requirements.txt

```See what code the robot wrote:

```bash

And you're good to go. Done!python debug_codegen.py

```

## Future Ideas

See what prices the robot is looking at:

I've got a bunch of ideas for what to add next:```bash

python debug_data.py

- More indicators like MACD, Bollinger Bands, ATR```

- Time-based rules so you can say "only trade between 9am-11am"

- Risk management like "don't lose more than $100"## � What Does the Robot Need? (Requirements)

- Multi-timeframe strategies where you check different time periods

- A web interface so you don't need to touch the code at allJust 3 things:

- The ability to save and load your strategies easily- **Lark** - Helps the robot understand languages

- Live trading with real money (that's the scary part!)- **Pandas** - Helps the robot read stock prices

- **NumPy** - Helps the robot do math

Some of these are simpler than others, but I'm excited to get to them eventually.

Install them all at once:

## Links and Stuff```bash

pip install -r requirements.txt

If you want to learn more about any of this:```

- Trading info: https://www.investopedia.com/

- The parser library: https://lark-parser.readthedocs.io/## 🚧 Cool Things We Want to Add! (Future Ideas)

- Data stuff: https://pandas.pydata.org/

- [ ] More tricks like MACD, Bollinger Bands

These are all really good resources if you get stuck or want to dive deeper.- [ ] Time-based rules ("Buy only between 9am-11am")

- [ ] Risk control ("Don't lose more than $100")

## Who Built This?- [ ] Multi-timeframe ("Check 1-hour AND 1-day charts")

- [ ] Web page where you can build strategies (no code needed!)

Just me, Varun Singh. Built it because I was tired of manually writing code for every trading idea I had. There's gotta be a better way, you know?- [ ] Save and load your strategies

- [ ] Live trading with real money (scary! 😱)

---

## 📖 Learn More

**Current Status**: Works great! The robot can understand what you say and trade automatically!

- Learn about stock trading: https://www.investopedia.com/

**Last Updated**: December 9, 2025- Lark (the parser): https://lark-parser.readthedocs.io/

- Pandas (data stuff): https://pandas.pydata.org/

## 👨‍💻 Who Made This?

**Varun Singh** - The person who created this robot trader!

---

**Current Status**: ✅ The Robot Works! It can understand what you say and trade automatically!

**Last Updated**: December 9, 2025
