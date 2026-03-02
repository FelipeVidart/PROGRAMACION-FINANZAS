from __future__ import annotations

from abc import ABC, abstractmethod
import pandas as pd

from felo_finance.risk.data.types import PricesRequest


class PriceProvider(ABC):
    """Interface for price data providers."""

    @abstractmethod
    def fetch(self, req: PricesRequest) -> pd.DataFrame:
        """
        Fetch raw price data.

        Expected output:
        - index: DatetimeIndex
        - columns: tickers (ideally)
        - values: prices (float)
        """
        raise NotImplementedError