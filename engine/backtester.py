# engine/backtester.py
import pandas as pd
from typing import List, Dict, Any

def run_backtest(df: pd.DataFrame, signals: pd.DataFrame) -> Dict[str, Any]:
    """
    Implements a simple long-only backtest simulation based on entry/exit signals.
    
    Args:
        df: DataFrame containing OHLCV data (indexed by date).
        signals: DataFrame with boolean 'entry' and 'exit' columns.
        
    Returns:
        Dictionary containing backtest results and metrics.
    """
    
    # Combine data and signals
    data = df.join(signals, how='left').fillna(False)
    
    # Initialize variables
    in_position = False
    equity_curve = [1.0] # Starting equity normalized to 1.0
    trades: List[Dict[str, Any]] = []
    current_trade: Dict[str, Any] = {}
    
    # Tracking for Drawdown calculation
    peak_equity = 1.0
    max_drawdown = 0.0
    
    # --- Simulation Loop ---
    for index, row in data.iterrows():
        
        # 1. Update daily equity (for drawdown calculation purposes)
        if in_position:
            # Calculate current PnL of the open trade
            daily_pnl = (row['CLOSE'] / current_trade['entry_price']) - 1.0
            
            # Simple equity calculation for tracking peak/drawdown
            # NOTE: This is a simplified equity tracking focused on realizing final metrics
            current_equity = equity_curve[-1] 
            
            # If the position is open, we need to track the return relative to the market
            # For simplicity in a trade-by-trade backtest, we primarily update equity only on trade exit.
            
        else:
            current_equity = equity_curve[-1]

        # 2. Check for ENTRY
        if row['entry'] and not in_position:
            in_position = True
            current_trade = {
                'entry_date': index,
                'entry_price': row['CLOSE'], # Entry price is CLOSE
                'exit_date': None,
                'exit_price': None,
                'profit_loss': None
            }

        # 3. Check for EXIT
        elif row['exit'] and in_position:
            in_position = False
            
            # Calculate PnL for the completed trade
            exit_price = row['CLOSE'] # Exit price is CLOSE
            pnl_return = (exit_price / current_trade['entry_price']) - 1.0 # Profit/loss
            
            # Update equity curve
            new_equity = equity_curve[-1] * (1 + pnl_return)
            equity_curve.append(new_equity)
            current_equity = new_equity
            
            # Finalize trade record
            current_trade['exit_date'] = index
            current_trade['exit_price'] = exit_price
            current_trade['profit_loss'] = pnl_return
            
            trades.append(current_trade)
            
            # Reset
            current_trade = {}

        # 4. Drawdown Calculation
        peak_equity = max(peak_equity, current_equity)
        drawdown = (peak_equity - current_equity) / peak_equity
        max_drawdown = max(max_drawdown, drawdown)
        
        
    # --- Final Reporting ---
    final_equity = equity_curve[-1]
    total_return = final_equity - 1.0 # Total return
    
    return {
        'total_return': f"{total_return * 100:.2f}%",
        'max_drawdown': f"{max_drawdown * 100:.2f}%",
        'number_of_trades': len(trades), # Number of trades
        'trade_log': trades
    }