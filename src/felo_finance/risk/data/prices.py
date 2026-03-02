from __future__ import annotations

from typing import Literal

import pandas as pd

from felo_finance.risk.data.types import PricesError, PricesRequest, PriceField
from felo_finance.risk.data.providers import YahooProvider, PriceProvider


ProviderName = Literal["yahoo"]

def _build_provider(name: ProviderName) -> PriceProvider:
    if name == "yahoo":
        return YahooProvider()
    raise PricesError(f"Unknown provider: {name}")


def get_prices(
    *,
    tickers: list[str] | str,
    start: str,
    end: str,
    interval: str = "1d",
    field: PriceField = "adj_close",
    provider: ProviderName = "yahoo",
) -> pd.DataFrame:
    """
    Provider-agnostic entry point to fetch prices.

    Returns a normalized DataFrame:
    - index: DatetimeIndex named 'date'
    - columns: tickers
    - values: float prices
    """
    if isinstance(tickers, str):
        tickers_list = [tickers]
    else:
        tickers_list = list(tickers)

    req = PricesRequest(
        tickers=tickers_list,
        start=start,
        end=end,
        interval=interval,
        field=field,
    )

    prov = _build_provider(provider)
    df = prov.fetch(req)

    # Final validation contract
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise PricesError("Provider returned empty/non-DataFrame result.")
    if not isinstance(df.index, pd.DatetimeIndex):
        raise PricesError("Prices index must be a DatetimeIndex.")
    if df.shape[1] < 1:
        raise PricesError("Prices must contain at least one ticker column.")

    return df