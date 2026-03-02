# Felo - Programacion en Finanzas

## Project Overview
Felo is a structured educational project for learning financial risk modeling and quantitative finance with Python.

The codebase follows professional practices (clean architecture, testing, modularity), but its primary purpose is learning, experimentation, and building strong foundations over time.

## Objectives
- Understand financial risk concepts deeply
- Implement core models from scratch
- Apply testing and modular architecture in practice
- Build a solid personal quantitative toolkit

## Repository Structure
```text
src/
  felo_finance/
    risk/
      data/
      measures/
tests/
```

## Installation
### 1. Create a virtual environment
```bash
python -m venv .venv
```

### 2. Activate the environment
Windows (PowerShell):
```bash
.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Install the project in editable mode
```bash
pip install -e .
```

## Running Tests
Run the full test suite:
```bash
pytest -q
```

Run integration tests separately:
```bash
pytest -q tests/integration
```

## Development Workflow
1. Design the financial model or risk concept to implement.
2. Implement the feature in the corresponding module.
3. Add or update tests (unit and/or integration).
4. Run `pytest -q` to validate behavior.
5. Commit and push changes.

## Roadmap
- Risk fundamentals (returns, volatility)
- Value at Risk (VaR)
- Expected Shortfall (ES)
- Monte Carlo simulation
- Backtesting

## Notes
This repository is intentionally evolving. It is not presented as a production-ready risk engine, but as a serious learning project built with professional structure and discipline.