# Cryptocurrency Price Forecasting

> **One‑command crypto forecasting** — ingest CSVs, train a linear regression, and export year‑by‑year predictions plus a multi‑page PDF of historical vs. projected trendlines.

This project demonstrates an end‑to‑end analytics workflow: clean data ingestion, simple but explainable modeling (scikit‑learn Linear Regression), and automated reporting (Matplotlib) to communicate results clearly.

---

## Key features
- Forecast yearly all‑time highs (YATH) for the next **10 years** for three cryptocurrencies.
- End‑to‑end Python pipeline: CSV ingestion → feature prep with **Pandas/NumPy** → linear regression with **scikit‑learn**.

- Automated outputs:
  - Year‑by‑year **`.txt`** predictions per asset
  - A multi‑page **Matplotlib PDF** comparing historical vs. projected trendlines

> ⚠️ **Not financial advice.** This is a learning/demo project — not a trading system.

---

## Quick start

### 1) Set up a virtual environment
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
Pick one of the following:

- **With `requirements.txt` (recommended for this repo):**
  ```bash
  pip install -r requirements.txt
  ```
**Expected columns (typical):** `date`, `close` (you can adjust in code).

### 3) Run the pipeline
```bash
python main.py
```

### 5) Review outputs
- **Text predictions:** per‑asset `.txt` files. Examples observed in this repo:
- `CEL-results.txt`
- `CRO-results.txt`
- `DFI-results.txt`
- **PDF report:** e.g., `prediction-plots.pdf`

---

## How it works (high level)
1. **Ingest** CSVs for the selected tickers.
2. **Transform** into model‑ready features with Pandas/NumPy.
3. **Train** a per‑asset `LinearRegression` (scikit‑learn).
4. **Project** the next 10 yearly all‑time highs.
5. **Export**:
   - Plain‑text prediction files (easy to diff & audit)
   - A multi‑page Matplotlib PDF visualizing history vs. projection

---

## Project structure 
- `main.py` — entry point; orchestrates ingestion, training, and exports
- `*.csv` — input price histories (examples included)
- `*-results.txt` — sample prediction outputs (generated)
- `prediction-plots.pdf` — sample multi‑page plot export

---

## Limitations
- Linear models on financial time series can **underfit** regime changes.
- Forecasts are **illustrative**, not probabilistic or risk‑aware.
- Data quality matters: missing values/outliers will affect the fit and plots.

---
