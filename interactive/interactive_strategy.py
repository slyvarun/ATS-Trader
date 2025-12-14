#!/usr/bin/env python3
"""
INTERACTIVE STRATEGY BUILDER
=============================

Type your trading strategy in plain English and watch it execute!
No code knowledge needed - just describe what you want.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.nl_parser import nl_to_dsl
from engine.dsl_parser import parse_dsl_to_ast
from engine.code_generator import generate_python_strategy
from engine.backtester import run_backtest
from engine.data_utils import load_data
from numpy import nan


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def print_section(title):
    """Print a section divider"""
    print("\n" + "-" * 70)
    print(title)
    print("-" * 70)


def print_success(message):
    """Print success message"""
    print(f"[OK] {message}")


def print_error(message):
    """Print error message"""
    print(f"[ERROR] {message}")


def print_info(message):
    """Print info message"""
    print(f"[INFO] {message}")


def show_examples():
    """Show example strategies"""
    print_header("EXAMPLE STRATEGIES")
    
    examples = [
        ("Moving Average", "Buy when close is above 20-day moving average and volume is above 1 million. Sell when close drops below 50-day moving average."),
        ("Breakout", "Enter when close is above 30-day moving average. Exit when close falls below 10-day moving average."),
        ("Volume Breakout", "Buy when volume is greater than 2 million and close price is above the 20-day moving average. Sell when volume drops below 500000."),
    ]
    
    for i, (name, desc) in enumerate(examples, 1):
        print(f"\n{i}. {name}:")
        print(f"   {desc}")
    
    print("\nYou can use similar phrases to describe your own strategy!")


def show_supported_phrases():
    """Show what English phrases are supported"""
    print_header("SUPPORTED ENGLISH PHRASES")
    
    print("\nPrice Fields:")
    print("  - close price, volume, high, low, open")
    
    print("\nComparison Operators:")
    print("  - above, below, greater than, less than, equal to")
    
    print("\nIndicators:")
    print("  - 20-day moving average, 50 day moving average")
    print("  - RSI(14), RSI(21)")
    
    print("\nLogic:")
    print("  - and, or (with any amount of parentheses)")
    
    print("\nNumbers:")
    print("  - 1 million, 2 million, 500000, etc.")
    
    print("\nEntry/Exit:")
    print("  - buy when, enter when, sell when, exit when")


def run_interactive_strategy():
    """Main interactive strategy builder"""
    
    print_header("INTERACTIVE TRADING STRATEGY BUILDER")
    print("\nWelcome! You can describe trading strategies in plain English.")
    print("The system will convert it to code and test it automatically.\n")
    
    while True:
        print("\n" + "=" * 70)
        print("MENU")
        print("=" * 70)
        print("1. Enter your strategy")
        print("2. See example strategies")
        print("3. See supported phrases")
        print("4. Exit")
        print()
        
        choice = input("Choose option (1-4): ").strip()
        
        if choice == "1":
            get_and_run_strategy()
        elif choice == "2":
            show_examples()
        elif choice == "3":
            show_supported_phrases()
        elif choice == "4":
            print("\nThank you for using ATS-Trader! Goodbye!\n")
            break
        else:
            print_error("Invalid choice. Please enter 1-4.")


def get_and_run_strategy():
    """Get strategy from user and run it"""
    
    print_header("ENTER YOUR STRATEGY")
    
    print("\nDescribe your strategy in English.")
    print("Example:")
    print('  "Buy when close is above 20-day moving average and volume is above 1 million.')
    print('   Sell when close drops below 50-day moving average."')
    print()
    
    print("Start typing (press Enter twice when done):")
    print("-" * 70)
    
    lines = []
    try:
        while True:
            line = input()
            if not line and lines and not lines[-1]:
                # Two consecutive empty lines - user is done
                lines.pop()  # Remove the last empty line
                break
            lines.append(line)
    except EOFError:
        # Handle Ctrl+D
        pass
    
    strategy = "\n".join(lines).strip()
    
    if not strategy:
        print_error("No strategy entered!")
        return
    
    print_section("YOUR STRATEGY")
    print(strategy)
    
    # Process the strategy
    process_strategy(strategy)


def process_strategy(strategy):
    """Process the strategy through the entire pipeline"""
    
    print_section("STEP 1: CONVERTING TO DSL")
    
    try:
        dsl = nl_to_dsl(strategy)
        print_success("Natural Language Parser")
        print(f"\nEntry Rule: {dsl['entry']}")
        print(f"Exit Rule:  {dsl['exit']}")
    except Exception as e:
        print_error(f"Failed to parse natural language: {e}")
        return
    
    print_section("STEP 2: PARSING DSL")
    
    try:
        dsl_text = f"{dsl['entry']} {dsl['exit']}"
        ast = parse_dsl_to_ast(dsl_text)
        print_success("DSL Parser (Lark Grammar)")
        print("Abstract Syntax Tree built successfully")
    except Exception as e:
        print_error(f"Failed to parse DSL: {e}")
        return
    
    print_section("STEP 3: GENERATING PYTHON CODE")
    
    try:
        code = generate_python_strategy(ast)
        print_success("Code Generator")
        print(f"\nGenerated {len(code)} lines of Python code")
        print("\nFirst 300 characters of generated code:")
        print("-" * 70)
        print(code[:300] + "...")
    except Exception as e:
        print_error(f"Failed to generate code: {e}")
        return
    
    print_section("STEP 4: LOADING DATA")
    
    try:
        df = load_data()
        print_success("Data Loader")
        print(f"Loaded {len(df)} rows of price data")
        print(f"Date range: {df.index[0]} to {df.index[-1]}")
        print(f"Columns: {', '.join(df.columns)}")
    except Exception as e:
        print_error(f"Failed to load data: {e}")
        return
    
    print_section("STEP 5: EXECUTING STRATEGY")
    
    try:
        exec_globals = {
            'DataFrame': __import__('pandas').DataFrame,
            'nan': nan,
            'calculate_sma': __import__('engine.data_utils', fromlist=['calculate_sma']).calculate_sma,
        }
        exec_scope = {}
        exec(code, exec_globals, exec_scope)
        calculate_signals_func = exec_scope['calculate_signals']
        signals = calculate_signals_func(df)
        print_success("Strategy Execution")
        print("Signals generated successfully")
    except Exception as e:
        print_error(f"Failed to execute strategy: {e}")
        return
    
    print_section("STEP 6: BACKTESTING")
    
    try:
        results = run_backtest(df, signals)
        print_success("Backtest Complete")
        
        # Convert to float if needed (remove % sign if present)
        total_return_str = results['total_return']
        if isinstance(total_return_str, str):
            total_return = float(total_return_str.replace('%', '').strip())
        else:
            total_return = float(total_return_str)
            
        max_drawdown_str = results['max_drawdown']
        if isinstance(max_drawdown_str, str):
            max_drawdown = float(max_drawdown_str.replace('%', '').strip())
        else:
            max_drawdown = float(max_drawdown_str)
            
        num_trades = int(results['number_of_trades']) if isinstance(results['number_of_trades'], str) else results['number_of_trades']
        
        print("\n" + "=" * 70)
        print("BACKTEST RESULTS")
        print("=" * 70)
        print(f"\nTotal Return:      {total_return:>10.2f}%")
        print(f"Max Drawdown:      {max_drawdown:>10.2f}%")
        print(f"Number of Trades:  {num_trades:>10}")
        
        if num_trades == 0:
            print_info("No trades were generated with this strategy on the test data")
        else:
            print_info(f"Strategy generated {num_trades} trades")
        
        print("\n" + "=" * 70)
        print("STRATEGY EXECUTION SUCCESSFUL!")
        print("=" * 70)
        
    except Exception as e:
        print_error(f"Failed to run backtest: {e}")
        import traceback
        traceback.print_exc()
        return


def quick_test_strategy(strategy_text):
    """Quick test - runs strategy without interactive prompts"""
    
    print_header("QUICK TEST MODE")
    print(f"\nStrategy: {strategy_text}\n")
    process_strategy(strategy_text)


if __name__ == "__main__":
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        # Quick test mode
        strategy = " ".join(sys.argv[1:])
        quick_test_strategy(strategy)
    else:
        # Interactive mode
        try:
            run_interactive_strategy()
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Goodbye!\n")
        except Exception as e:
            print_error(f"Unexpected error: {e}")
            import traceback
            traceback.print_exc()
