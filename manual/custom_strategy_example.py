#!/usr/bin/env python3
"""
CUSTOM STRATEGY EXAMPLE
=======================

This shows how YOU can write your own trading strategies in plain English!
Just write what you want, and the system converts it automatically.

No need to learn the DSL - just speak naturally!
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.nl_parser import nl_to_dsl
from engine.dsl_parser import parse_dsl_to_ast
from engine.code_generator import generate_python_strategy
from engine.backtester import run_backtest
from engine.data_utils import load_data
import pandas as pd
from numpy import nan


def run_custom_strategy(english_description):
    """
    Takes a plain English strategy description and runs it!
    
    Args:
        english_description (str): Your strategy in plain English
    
    Returns:
        dict: Results with signals, returns, and drawdown
    """
    
    print("=" * 70)
    print("🎯 YOUR ENGLISH STRATEGY")
    print("=" * 70)
    print(english_description)
    print()
    
    # Step 1: Convert English to DSL
    print("=" * 70)
    print("📝 CONVERTED TO DSL")
    print("=" * 70)
    dsl_code = nl_to_dsl(english_description)
    print(f"Entry Rule:  {dsl_code['entry']}")
    print(f"Exit Rule:   {dsl_code['exit']}")
    print()
    
    # Step 2: Parse DSL to AST
    print("=" * 70)
    print("🔧 PARSED TO AST")
    print("=" * 70)
    try:
        dsl_text = f"{dsl_code['entry']} {dsl_code['exit']}"
        ast = parse_dsl_to_ast(dsl_text)
        print("✅ Strategy parsed successfully!")
        print()
    except Exception as e:
        print(f"❌ Error parsing strategy: {e}")
        return None
    
    # Step 3: Generate Python code
    print("=" * 70)
    print("💻 GENERATED PYTHON CODE")
    print("=" * 70)
    try:
        python_code = generate_python_strategy(ast)
        print("First 500 characters of generated code:")
        print(python_code[:500])
        print("...")
        print()
    except Exception as e:
        print(f"❌ Error generating code: {e}")
        return None
    
    # Step 4: Load sample data
    print("=" * 70)
    print("📊 LOADING SAMPLE DATA")
    print("=" * 70)
    df = load_data()
    print(f"Loaded {len(df)} rows of sample price data")
    print(f"Columns: {', '.join(df.columns)}")
    print()
    
    # Step 5: Run backtest
    print("=" * 70)
    print("📈 RUNNING BACKTEST")
    print("=" * 70)
    try:
        # Create a globals dict with necessary imports for the exec environment
        exec_globals = {
            'DataFrame': __import__('pandas').DataFrame,
            'nan': nan,
            'calculate_sma': __import__('engine.data_utils', fromlist=['calculate_sma']).calculate_sma,
        }
        # Execute the generated code
        exec_scope = {}
        exec(python_code, exec_globals, exec_scope)
        calculate_signals_func = exec_scope['calculate_signals']
        signals = calculate_signals_func(df)
        
        # Run backtest
        results = run_backtest(df, signals)
        total_return = float(results['total_return']) if isinstance(results['total_return'], str) else results['total_return']
        max_drawdown = float(results['max_drawdown']) if isinstance(results['max_drawdown'], str) else results['max_drawdown']
        num_trades = int(results['number_of_trades']) if isinstance(results['number_of_trades'], str) else results['number_of_trades']
        
        print(f"Total Return:     {total_return:.2f}%")
        print(f"Max Drawdown:     {max_drawdown:.2f}%")
        print(f"Number of Trades: {num_trades}")
        print(f"Status:           Success!")
        print()
        return results
    except Exception as e:
        print(f"❌ Error running backtest: {e}")
        import traceback
        traceback.print_exc()
        return None


# ============================================================================
# EXAMPLE STRATEGIES - Try these or write your own!
# ============================================================================

if __name__ == "__main__":
    
    print("\n" + "🎉" * 35)
    print("WELCOME TO CUSTOM STRATEGY BUILDER")
    print("🎉" * 35 + "\n")
    
    # ---- STRATEGY 1: Simple Moving Average ----
    strategy_1 = """
    Buy when the close price is above the 20-day moving average 
    and the volume is greater than 1 million. 
    Sell when the close price drops below the 50-day moving average.
    """
    
    print("\n>>> RUNNING STRATEGY 1: Simple Moving Average Strategy")
    run_custom_strategy(strategy_1)
    
    # ---- STRATEGY 2: Breakout Strategy ----
    strategy_2 = """
    Enter when close is above 30-day moving average.
    Exit when close falls below 10-day moving average.
    """
    
    print("\n>>> RUNNING STRATEGY 2: Breakout Strategy")
    run_custom_strategy(strategy_2)
    
    # ---- STRATEGY 3: High Volume Strategy ----
    strategy_3 = """
    Buy when volume is greater than 2 million and close price is above 20-day average.
    Sell when volume drops below 500000.
    """
    
    print("\n>>> RUNNING STRATEGY 3: High Volume Strategy")
    run_custom_strategy(strategy_3)
    
    # ============================================================================
    # TRY YOUR OWN STRATEGY!
    # ============================================================================
    
    print("\n" + "=" * 70)
    print("💡 TRY YOUR OWN STRATEGY")
    print("=" * 70)
    print("""
You can write any strategy using these words:
  - Prices: close price, volume, high, low, open
  - Comparisons: above, below, greater than, less than, equal to
  - Indicators: 20-day moving average, RSI(14)
  - Logic: and, or
  - Actions: buy, enter, sell, exit
  
Example:
    "Buy when close is above 50-day moving average and volume is high.
     Sell when close drops below 20-day moving average."
     
Just uncomment the code below and write your own!
    """)
    
    # Uncomment this and write your own strategy!
    # my_strategy = """
    # Your English strategy here...
    # """
    # run_custom_strategy(my_strategy)
    
    print("\n✨ Done! Feel free to create more strategies! ✨\n")
