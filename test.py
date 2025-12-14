# run_demo.py - The final end-to-end demonstration script.

# Import all modules from the engine
from engine.nl_parser import nl_to_dsl
from engine.dsl_parser import parse_dsl_to_ast
from engine.code_generator import generate_python_strategy
from engine.backtester import run_backtest # Assuming this is implemented now
from engine.data_utils import load_data 
import json
from numpy import nan

# --- 1. Define Natural Language Input ---
SAMPLE_NL = "Buy when the close price is above the 20-day moving average and volume is above 1 million. Exit when close is less than the 50-day moving average."

print("\n\n#####################################################")
print("### ATS Trader: End-to-End Strategy Execution Demo ###")
print("#####################################################")

try:
    # --- 2. NL -> DSL ---
    print("\n[1] Natural Language Input:")
    print(f"    '{SAMPLE_NL}'") 

    dsl_output = nl_to_dsl(SAMPLE_NL)
    dsl_text = f"{dsl_output['entry']} {dsl_output['exit']}" 

    print("\n[2] Generated DSL:")
    print(f"    {dsl_output['entry']}")
    print(f"    {dsl_output['exit']}")

   # run_demo.py (Corrected AST Printing Block)

    # --- 3. DSL -> AST ---
    ast_output = parse_dsl_to_ast(dsl_text) 
    
    print("\n[3] Parsed AST (Entry Excerpt):")
    try:
    # 1. Attempt to print the successfully transformed dictionary
        print(json.dumps(ast_output['entry'], indent=2))
    
    except TypeError:
    # 2. If printing fails (due to the Tree object), print the warning and let the script continue.
    # The 'TypeError' is the final confirmation that parsing succeeded but visualization failed.
        print("WARNING: AST visualization failed due to serialization error. Proceeding to execution...")
    
#   NOTE: There should be NO extra print(json.dumps(...)) line here.
    # --- 4. AST -> Python Code Generation ---
    strategy_code = generate_python_strategy(ast_output)

    # --- 5. Code Execution and Signal Generation ---
    df = load_data() 
    exec_scope = {}
    # Create a globals dict with necessary imports for the exec environment
    exec_globals = {
        'DataFrame': __import__('pandas').DataFrame,
        'nan': __import__('numpy').nan,
        'calculate_sma': __import__('engine.data_utils', fromlist=['calculate_sma']).calculate_sma,
    }
    # Execute the generated string to define the calculate_signals function
    exec(strategy_code, exec_globals, exec_scope) 
    calculate_signals_func = exec_scope['calculate_signals']
    signals = calculate_signals_func(df) 
    print("[5] Signals Generated Successfully.")

    # --- 6. Backtest Simulation ---
    backtest_result = run_backtest(df, signals) 

    # --- 7. Final Report ---
    print("\n####################")
    print("# Backtest Results #")
    print("####################")
    print(f"Total Return:     {backtest_result['total_return']}")
    print(f"Max Drawdown:     {backtest_result['max_drawdown']}")
    print(f"Number of Trades: {backtest_result['number_of_trades']}")

    if backtest_result['trade_log']:
        print("\nEntry/Exit Log (First Trade):")
        trade = backtest_result['trade_log'][0]
        # Assuming run_backtest formats dates and prices correctly
        print(f"  Enter: {trade['Enter Date']} at {trade['Enter Price']}")
        print(f"  Exit:  {trade['Exit Date']} at {trade['Exit Price']}")

    print("\nDemo Complete.")
    
except ValueError as e:
    print(f"\n❌ FATAL TEST FAILED (Validation Error): {e}")
    print("\nCheck your NL-to-DSL conversion and DSL Grammar for exact token matches.")
except Exception as e:
    print(f"\n❌ UNEXPECTED ERROR: {e}")