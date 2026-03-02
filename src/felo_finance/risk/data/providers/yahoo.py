from __future__ import annotations

import pandas as pd
import yfinance as yf

from felo_finance.risk.data.providers.base import PriceProvider
from felo_finance.risk.data.types import PricesError, PricesRequest


class YahooProvider(PriceProvider):
    """
    Yahoo Finance provider via yfinance.

    Notes:
    - yfinance returns either:
      - Single ticker: columns like ["Open","High","Low","Close",...]
      - Multiple tickers: MultiIndex columns (field, ticker)
    """

    def fetch(self, req: PricesRequest) -> pd.DataFrame:
        if not req.tickers:
            raise PricesError("tickers cannot be empty")

        tickers = req.tickers if len(req.tickers) > 1 else req.tickers[0]

        df = yf.download(
            tickers,
            start=req.start,
            end=req.end,
            interval=req.interval,
            auto_adjust=False,   # dejamos el ajuste explícito por field
            progress=False,
            group_by="column",
        )

        if df is None or df.empty:
            raise PricesError("No data returned from Yahoo Finance.")

        # Normalize to a (date x tickers) DataFrame with the requested field
        field_map = {"close": "Close", "adj_close": "Adj Close"}
        wanted = field_map[req.field]

        if isinstance(df.columns, pd.MultiIndex):
            # MultiIndex columns: level 0 = field, level 1 = ticker
            if wanted not in df.columns.get_level_values(0):
                raise PricesError(f"Yahoo data missing field '{wanted}'.")
            out = df[wanted].copy()
        else:
            # Single ticker: columns are fields
            if wanted not in df.columns:
                raise PricesError(f"Yahoo data missing field '{wanted}'.")
            out = df[[wanted]].copy()
            out.columns = req.tickers  # renombramos a ticker real

        out.index = pd.to_datetime(out.index)
        out.index.name = "date"
        out = out.sort_index()

        # Coerce numeric
        for c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce")

        # Drop columns fully NaN (ticker que no bajó)
        out = out.dropna(axis=1, how="all")

        if out.empty:
            raise PricesError("All downloaded series are empty after cleaning.")

        return out