import pandas as pd

from felo_finance.risk.data.prices import get_prices


def test_get_prices_returns_dataframe(monkeypatch):
    # Fake provider fetch() output
    fake = pd.DataFrame(
        {"AAPL": [100.0, 101.0], "MSFT": [200.0, 202.0]},
        index=pd.to_datetime(["2024-01-01", "2024-01-02"]),
    )
    fake.index.name = "date"

    # Monkeypatch the YahooProvider.fetch to return fake data
    from felo_finance.risk.data.providers.yahoo import YahooProvider

    def _fake_fetch(self, req):
        return fake

    monkeypatch.setattr(YahooProvider, "fetch", _fake_fetch)

    df = get_prices(tickers=["AAPL", "MSFT"], start="2024-01-01", end="2024-01-03")
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["AAPL", "MSFT"]
    assert df.shape == (2, 2)