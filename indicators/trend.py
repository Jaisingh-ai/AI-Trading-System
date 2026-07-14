import pandas as pd


class TrendIndicator:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate_ema(self):

        self.df["EMA20"] = (
            self.df["Close"]
            .ewm(span=20, adjust=False)
            .mean()
        )

        self.df["EMA50"] = (
            self.df["Close"]
            .ewm(span=50, adjust=False)
            .mean()
        )

        return self.df

    def get_trend(self):

        self.calculate_ema()

        ema20 = self.df["EMA20"].iloc[-1]
        ema50 = self.df["EMA50"].iloc[-1]

        if ema20 > ema50:
            return "BULLISH"

        elif ema20 < ema50:
            return "BEARISH"

        return "SIDEWAYS"