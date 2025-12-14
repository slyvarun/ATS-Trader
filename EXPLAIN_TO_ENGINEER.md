# ATS-Trader — Technical Walkthrough for an Experienced Engineer

This document is a concise, by-the-numbers explanation you can read aloud to a technical colleague. It covers architecture, the NL→DSL→AST→code pipeline, file-level responsibilities, known issues, demo commands, and recommended next steps.

## Opening (30–60s)
- Quick statement of purpose: this repo implements a pipeline that converts plain-English trading strategies into executable Python strategy code and runs a simple backtest.
- High-level goal: enable rapid strategy prototyping with an interpretable intermediate representation (DSL) and a readable generated Python implementation.

## Architecture at a glance (1–2 minutes)
- Top-level layout:
  - `engine/` — core pipeline and domain libraries (NL parser, DSL parser, code generator, backtester, data utilities).
  - `interactive/` — CLI-driven interactive strategy builder with a six-step execution display.
  - `manual/` — templates and examples for advanced users who prefer editing files.
  - Root docs and guides for onboarding.
- Design principle: strict separation of concerns — parsing (NL, DSL), AST representation, codegen, data & indicators, and execution/backtesting.

## End-to-end flow (2–3 minutes)
The runtime pipeline implemented is:

1. Natural Language Parser (`engine/nl_parser.py`)
   - Input: arbitrary English strategy sentences.
   - Output: an intermediate DSL string formatted as `ENTRY: <rule_set> EXIT: <rule_set>`.
   - Responsibilities: tokenization, normalization, number parsing ("2 million" → 2000000), indicator extraction (detects "20-day moving average"), synonym handling ("drops/falls/goes"), and phrase-to-DSL mapping.

2. DSL Parser (`engine/dsl_parser.py`)
   - Uses Lark (LALR) with an explicit grammar. Produces a deterministic AST (dict with `entry` and `exit` trees).
   - Grammar highlights: `strategy: "ENTRY:" rule_set "EXIT:" rule_set` with `rule_set` supporting logical combinations and nested parentheses.

3. Code Generator (`engine/code_generator.py`)
   - Translates AST into a `calculate_signals(df: DataFrame) -> DataFrame` function using vectorized Pandas operations.
   - Strategy: precompute indicators, then compute boolean expressions for comparisons and combine them with bitwise ops (`&`/`|`).

4. Data Utilities (`engine/data_utils.py`)
   - Sample price loader (used for quick tests) and indicator helpers (SMA, RSI). Indicator helpers return aligned Series to be consumed by generated code.

5. Backtester (`engine/backtester.py`)
   - Light event-loop simulation that walks rows, toggles `in_position` on entry/exit signals, records trades, computes metrics (total return, max drawdown, trade count).
   - Simple assumptions: no slippage, full-size fills, no commission (easy to extend).

6. Interactive CLI (`interactive/interactive_strategy.py`)
   - Orchestrates the above and prints six steps: NL → DSL → AST → generated code → data load → execute → backtest.
   - Offers quick-test mode for single-sentence runs and menu-driven mode for multi-step interaction.

## File-level responsibilities and important internals (4–6 minutes)

- `engine/nl_parser.py`
  - Important implementation notes:
    - Indicator detection runs before removal of filler words to avoid losing tokens like "20-day".
    - Numbers are normalized, including magnitude keywords (million/billion).
    - If the user supplies no explicit exit clause, the parser now emits an always-false but parseable expression `0 > 1` (instead of the word `FALSE`) so the DSL grammar remains valid.

- `engine/dsl_parser.py`
  - Lark grammar intentionally keeps `FIELD` and `INDICATOR_NAME` as separate terminals to avoid token ambiguity.
  - Transformer (`StrategyTransformer`) returns a simple nested dict AST containing `comparison` and `binary_op` nodes.

- `engine/code_generator.py`
  - Generates pure-Pandas code. Contract:
    - Input DataFrame: index = datetime, columns = OPEN, HIGH, LOW, CLOSE, VOLUME.
    - Output: DataFrame with boolean columns for entry/exit signals; generator calls indicator helper functions from `data_utils` when needed.
  - Generated code is printed in the interactive flow for inspection; the generator aims for readability to allow manual review.

- `engine/data_utils.py`
  - Contains sample loader used for tests (25 rows) and helper functions (SMA/RSI).
  - For production, replace the loader with a connector to a proper OHLCV dataset (CSV, DB, or REST API) with consistent timezone handling.

- `engine/backtester.py`
  - Joins signals with price data, fills NaNs with `False`, then simulates position entries/exits.
  - Returns a simple results object with metrics and trade list. Easy to extend for position sizing and cost models.

## Demo / live commands (PowerShell)
Run these during the demo to show the end-to-end flow and inspect generated code.

Quick interactive test (from the `interactive` folder):

```powershell
cd "C:\Users\VARUN\OneDrive\Desktop\projects\AST-Trader\ATS-Trader\interactive"
python interactive_strategy.py "buy when close above 100"
```

Expected outcome: the CLI prints six steps with [OK] markers, shows the generated code preview, and prints a short backtest summary (Total Return, Max Drawdown, Number of Trades). For the included sample data the strategy may produce zero trades — the important verification is that the flow executes without errors and prints each stage.

Run a manual example (from the `manual` folder):

```powershell
cd "C:\Users\VARUN\OneDrive\Desktop\projects\AST-Trader\ATS-Trader\manual"
python custom_strategy.py
```

If/when we add pytest-based unit tests, run them with:

```powershell
cd "C:\Users\VARUN\OneDrive\Desktop\projects\AST-Trader\ATS-Trader"
python -m pytest -q
```

## Important design decisions & tradeoffs

- DSL-first approach: gives a typed intermediate representation that is easy to validate and transform. The DSL's grammar produces clear parse errors and a predictable AST.
- Lark (LALR) was chosen for deterministic parsing and a straightforward Transformer API.
- Code generation (Pandas) was chosen for performance and clarity; generated code is human-readable and can be exported for inspection.
- Simplifications: backtester omits costs/slippage; NL parser accepts many natural forms but is not a full natural-language AI — it's deterministic rule-based mapping.

## Known issues & mitigations

- `EXIT: FALSE` vs grammar: earlier versions emitted `EXIT: FALSE` which failed the DSL parser; the pragmatic fix emits `EXIT: 0 > 1`. Long-term: add boolean literals to the grammar.
- Executing generated Python: currently executed locally; for any multi-user or production setup, sandbox the execution (containers, resource limits) or interpret AST instead of exec.
- Large datasets: generator assumes vectorized ops; memory usage can increase for very long histories — consider chunked or rolling-window evaluation for scale.

## Quality gates and tests (recommended)

- Add unit tests for:
  - `engine/nl_parser.py`: mapping several NL examples to expected DSL outputs.
  - `engine/dsl_parser.py`: parse coverage for indicators, nested logic, and operators.
  - `engine/code_generator.py`: small ASTs → generated code correctness using a tiny DataFrame.
  - `engine/backtester.py`: deterministic signal sets → expected PnL and trade counts.
- Add CI (GitHub Actions) to run linting and tests on PRs.

## Security note
- The system synthesizes and executes Python code. Never run arbitrary, untrusted NL input in a shared or production environment without sandboxing. Consider converting AST to a safe internal interpreter for multi-tenant deployments.

## Extension roadmap (short list)

1. Convert `engine/` into a proper Python package (`engine/__init__.py`) and remove ad-hoc `sys.path` inserts so scripts import naturally.
2. Add unit tests and GitHub Actions CI.
3. Extend backtester with transaction costs, slippage, and position sizing.
4. Add realistic data loaders and a small set of labeled datasets for regression testing of strategies.
5. Consider a Notebook/web UI for easier strategy authoring and interactive plots of P&L.

## Short demo plan (2–3 minutes)
1. Run the quick interactive test shown above and show the [OK] step outputs.
2. Show the generated Python snippet printed by the interactive script.
3. Explain how to extend indicators by adding a helper to `engine/data_utils.py` and registering the indicator name/token in `engine/dsl_parser.py`.

---

If you want, I can:
- Convert `engine/` into a proper package now and remove `sys.path` inserts (I can do this and re-run the quick test), or
- Scaffold pytest unit tests for the NL and DSL parsers and run them.

Tell me which you want and I will implement it next.
