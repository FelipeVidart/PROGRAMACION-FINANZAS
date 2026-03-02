import pytest

from felo_finance.risk.data import get_prices

pytestmark = pytest.mark.integration


def test_yahoo_download_real():
    df = get_prices(
        tickers=["AAPL", "MSFT"],
        start="2024-01-01",
        end="2024-02-01",
        provider="yahoo",
        field="adj_close",
    )
    assert not df.empty
    assert "AAPL" in df.columns