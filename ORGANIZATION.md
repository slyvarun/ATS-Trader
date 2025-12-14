# 📁 Project Organization

## Folder Structure

```
ATS-Trader/
├── engine/                      ← Core system (don't edit)
│   ├── nl_parser.py
│   ├── dsl_parser.py
│   ├── code_generator.py
│   ├── backtester.py
│   ├── data_utils.py
│   └── __pycache__/
│
├── interactive/                 ← Interactive mode
│   ├── README.md
│   ├── interactive_strategy.py
│   ├── INTERACTIVE_QUICK_START.md
│   ├── INTERACTIVE_GUIDE.md
│   ├── INTERACTIVE_COMPLETE.md
│   └── README_INTERACTIVE.md
│
├── manual/                      ← Manual mode
│   ├── README.md
│   ├── custom_strategy.py
│   ├── custom_strategy_example.py
│   ├── HOW_TO_USE_CUSTOM_STRATEGIES.md
│   └── USER_INPUT_GUIDE.md
│
├── test.py                      ← Run tests
├── README.md                    ← Project overview
├── dsl_spec.md                  ← Language specification
├── requirements.txt             ← Dependencies
├── DOCUMENTATION_INDEX.md       ← Documentation index
├── START_HERE.md                ← Quick start
└── COMPLETE_SUMMARY.md          ← Full summary
```

---

## 🎯 Two Ways to Use ATS-Trader

### Interactive Mode (Recommended for Beginners)

**Location:** `/interactive/`

**How to use:**
```bash
cd interactive
python interactive_strategy.py
```

**Features:**
- ✅ Menu-driven interface
- ✅ Type strategies directly
- ✅ See examples in the app
- ✅ No file editing needed
- ✅ Instant results

**Best for:**
- First-time users
- Quick testing
- Learning by example
- No file management

---

### Manual Mode (For Advanced Users)

**Location:** `/manual/`

**How to use:**
```bash
cd manual
python custom_strategy.py
```

Or create your own file and run it.

**Features:**
- ✅ Edit Python files
- ✅ Full control
- ✅ Save multiple strategies
- ✅ Integrate with your code
- ✅ Version control friendly

**Best for:**
- Experienced users
- Multiple strategies
- Code integration
- File-based workflows

---

## 📚 Documentation

### Quick Reference
- **START_HERE.md** - 5-minute overview (in root)
- **interactive/README.md** - Interactive mode guide
- **manual/README.md** - Manual mode guide

### Detailed Guides
- **interactive/INTERACTIVE_QUICK_START.md** - Interactive 2-min quick start
- **interactive/INTERACTIVE_GUIDE.md** - Interactive detailed guide
- **manual/HOW_TO_USE_CUSTOM_STRATEGIES.md** - Manual detailed guide

### Complete Documentation
- **COMPLETE_SUMMARY.md** - Full system summary
- **DOCUMENTATION_INDEX.md** - Complete index
- **README.md** - Project overview
- **dsl_spec.md** - DSL specification

---

## 🚀 Quick Start

### I'm New Here

1. Read: `START_HERE.md`
2. Choose interactive or manual mode
3. Follow the guide in that folder

### I Want Interactive Mode

```bash
cd interactive
python interactive_strategy.py
```

Then choose option 1 and type your strategy!

### I Want Manual Mode

```bash
cd manual
nano custom_strategy.py
# Edit your strategy
python custom_strategy.py
```

### I Want to Verify Everything Works

```bash
python test.py
```

Shows the complete pipeline working! ✅

---

## 🎮 Interactive Mode

**File:** `interactive/interactive_strategy.py`

**Run:**
```bash
python interactive/interactive_strategy.py
```

**Menu:**
```
1. Enter your strategy      ← Type directly
2. See examples             ← Learn from 3 examples
3. See supported phrases    ← Reference guide
4. Exit                     ← Quit
```

**Alternative - Quick Test:**
```bash
python interactive/interactive_strategy.py "Your strategy here"
```

---

## ✏️ Manual Mode

**Files:**
- `custom_strategy.py` - Main file with 3 examples
- `custom_strategy_example.py` - Alternative examples

**Run:**
```bash
python manual/custom_strategy.py
```

**Edit:**
```python
# Open custom_strategy.py and modify:
my_strategy = """
Your strategy here in English
"""
run_custom_strategy(my_strategy)
```

---

## 🔧 Core Engine (Don't Edit!)

**Location:** `engine/`

**Components:**
- `nl_parser.py` - Natural Language to DSL
- `dsl_parser.py` - DSL to AST parsing
- `code_generator.py` - AST to Python code
- `backtester.py` - Backtest engine
- `data_utils.py` - Data loading and indicators

These are the brain of the system. Don't modify unless you know what you're doing!

---

## 📋 What Gets Removed?

Cleaned up files:
- ❌ `debug_codegen.py` - Debug helper
- ❌ `debug_data.py` - Debug helper
- ❌ `run_demo.py` - Old demo
- ❌ `DOCUMENTATION_SIMPLIFIED.md` - Old doc
- ❌ `DOCUMENTATION_HUMAN_WRITTEN.md` - Old doc
- ❌ `DOCUMENTATION_REWRITE_SUMMARY.md` - Old doc
- ❌ `DOCUMENTATION_UPDATE.md` - Old doc
- ❌ `ANSWER_USER_INPUT.md` - Old doc

---

## ✅ Essential Files

**To Keep:**
- ✅ `engine/` - Core system
- ✅ `interactive/` - Interactive mode
- ✅ `manual/` - Manual mode
- ✅ `test.py` - Verification
- ✅ `requirements.txt` - Dependencies
- ✅ Documentation files

---

## 🎯 Which Mode to Use?

### Use Interactive Mode If:
- ✅ First time using ATS-Trader
- ✅ Want instant results without file editing
- ✅ Learning what's possible
- ✅ Quick testing
- ✅ Prefer menu-driven interface

### Use Manual Mode If:
- ✅ Want to save multiple strategies
- ✅ Prefer using your editor
- ✅ Need to integrate with code
- ✅ Want version control
- ✅ Advanced Python user

---

## 📖 Documentation Flow

```
START_HERE.md
    ↓
Choose Interactive or Manual
    ↓
If Interactive:
  → interactive/README.md
  → interactive/INTERACTIVE_QUICK_START.md
  → interactive/interactive_strategy.py
    ↓
If Manual:
  → manual/README.md
  → manual/custom_strategy.py
  → manual/HOW_TO_USE_CUSTOM_STRATEGIES.md
```

---

## 🚀 Getting Started

### Step 1: Navigate to Your Mode
```bash
# Interactive
cd interactive

# OR Manual
cd manual
```

### Step 2: Read the README
```bash
cat README.md
```

### Step 3: Run the System
```bash
# Interactive
python interactive_strategy.py

# OR Manual
python custom_strategy.py
```

### Step 4: Try a Strategy
```
Type or edit your strategy in English and execute!
```

---

## 💡 Key Points

✅ **Interactive Mode**
- Easier for beginners
- No file editing
- Menu-driven
- See examples in the app

✅ **Manual Mode**
- More control
- Save strategies
- Python flexibility
- Version control ready

✅ **Core Engine**
- Automatic conversion
- NL → DSL → AST → Code
- All steps transparent
- Production quality

✅ **Documentation**
- Quick starts in each folder
- Detailed guides included
- Examples provided
- Complete reference

---

## 🎉 You're All Set!

The project is now organized:
- 📁 **interactive/** - For interactive users
- 📁 **manual/** - For file-based users
- 📁 **engine/** - Core system
- 📄 **README files** - In each folder
- 🧹 **Cleaned up** - Old files removed

**Start here:** `START_HERE.md` or go directly to your preferred mode!

---

**Questions?** Check the README in your mode folder! 🚀
