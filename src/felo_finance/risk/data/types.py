from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


class PricesError(ValueError):
    """Raised when prices cannot be loaded or validated."""


PriceField = Literal["close", "adj_close"]


@dataclass(frozen=True)
class PricesRequest:
    tickers: list[str]
    start: str  # YYYY-MM-DD (por ahora)
    end: str    # YYYY-MM-DD
    interval: str = "1d"
    field: PriceField = "adj_close"