# Crypto predictions project (linear regression)

Forecast **yearly all‑time highs (YATH)** for a small set of cryptocurrencies using a simple, explainable **linear regression** model. The script ingests historical OHLCV CSVs, computes one ATH per year, fits `sklearn.linear_model.LinearRegression`, then exports:

- Per‑asset **text predictions** (`*-results.txt`)
- A multi‑page **PDF report** (`prediction-plots.pdf`) with historical vs. projected trendlines

> **Not financial advice.** This is a learning/demo project — not a trading system.

---

## What’s included

- `main.py` — pipeline entrypoint
- `CEL-USD.csv`, `CRO-USD.csv`, `DFI-USD.csv` — example input datasets
- `*-results.txt` — example outputs (generated)
- `prediction-plots.pdf` — example multi‑page plot output (generated)

---

## Quick start

### 1) Create a virtual environment (recommended)

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

This repo contains a `requirements.txt`. Install from it:

```bash
py -m pip install -r requirements.txt
```

> If you run into dependency bloat/conflicts, `main.py` only needs a small core set: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `scipy`.

### 3) Run

Run from the project root (so relative CSV paths work):

```bash
py main.py
```

When it finishes you should see `Done` printed.

---

## Input data format

`main.py` expects CSVs with at least these columns:

- **`Date`**: in `YYYY-MM-DD` format
- **`High`**: numeric daily high price

The included sample files follow the common Yahoo Finance-style OHLCV schema (Date/Open/High/Low/Close/Adj Close/Volume).

---

## Configuration

In `main.py`, the assets are configured by these lists:

- `files = ["DFI-USD.csv","CRO-USD.csv","CEL-USD.csv"]`
- `ticker_symbols = ["DFI","CRO","CEL"]`
- `result_file_names = ["DFI-results.txt","CRO-results.txt","CEL-results.txt"]`

To add/remove coins, update all three lists in sync and add the corresponding CSV file(s).

---

## Outputs

After running, you’ll get:

- **`*-results.txt`**: year-by-year predictions per asset
- **`prediction-plots.pdf`**: a page per asset with:
  - historical yearly ATH points
  - predicted future yearly ATH points

### Important note about repeat runs

The script **appends** to `*-results.txt` (it does not overwrite). If you want clean output per run, delete the old result files before rerunning.

---

## How it works (high level)

1. Read each CSV with Pandas.
2. Compute **one value per year**: the maximum daily `High` in that year.
3. Fit `LinearRegression` with \(X=\) year and \(y=\) yearly ATH.
4. Predict a future year range and export:
   - plain-text results
   - plotted trendlines to a multi-page PDF

---

## Limitations

- Linear trends can **underfit** regime changes and non-linear cycles common in crypto.
- The output is **illustrative**, not probabilistic, and does not include uncertainty bounds.

---

## Reference

- Pwned Passwords is not used here; this project is purely local modeling + plotting.
- Model: `sklearn.linear_model.LinearRegression`
