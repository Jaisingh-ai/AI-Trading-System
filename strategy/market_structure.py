import pandas as pd


class MarketStructure:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def find_swing_highs(self):

        swing_highs = []

        for i in range(2, len(self.df) - 2):

            current = self.df["High"].iloc[i]

            if (
                current > self.df["High"].iloc[i - 1]
                and current > self.df["High"].iloc[i - 2]
                and current > self.df["High"].iloc[i + 1]
                and current > self.df["High"].iloc[i + 2]
            ):

                swing_highs.append(i)

        return swing_highs

    def find_swing_lows(self):
        pass

    def detect_trend(self):
        pass

    def detect_bos(self):
        pass

    def detect_choch(self):
        pass