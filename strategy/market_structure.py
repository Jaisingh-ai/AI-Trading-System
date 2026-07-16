import pandas as pd


class MarketStructure:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    # ==========================================
    # Swing High Detection
    # ==========================================

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

                swing_highs.append(
                    {
                        "index": i,
                        "time": self.df.index[i],
                        "price": float(current),
                        "type": "Swing High",
                    }
                )

        return swing_highs

    # ==========================================
    # Swing Low Detection
    # ==========================================

    def find_swing_lows(self):

        swing_lows = []

        for i in range(2, len(self.df) - 2):

            current = self.df["Low"].iloc[i]

            if (
                current < self.df["Low"].iloc[i - 1]
                and current < self.df["Low"].iloc[i - 2]
                and current < self.df["Low"].iloc[i + 1]
                and current < self.df["Low"].iloc[i + 2]
            ):

                swing_lows.append(
                    {
                        "index": i,
                        "time": self.df.index[i],
                        "price": float(current),
                        "type": "Swing Low",
                    }
                )

        return swing_lows

    # ==========================================
    # Merge Swings
    # ==========================================

    def merge_swings(self):

        swing_highs = self.find_swing_highs()
        swing_lows = self.find_swing_lows()

        all_swings = swing_highs + swing_lows
        all_swings.sort(key=lambda x: x["time"])

        return all_swings

    # ==========================================
    # Market Structure
    # ==========================================

    def classify_market_structure(self):

        swing_highs = self.find_swing_highs()
        swing_lows = self.find_swing_lows()

        structure = []

        # Higher High / Lower High
        for i in range(1, len(swing_highs)):

            previous = swing_highs[i - 1]
            current = swing_highs[i]

            if current["price"] > previous["price"]:
                label = "HH"
            elif current["price"] < previous["price"]:
                label = "LH"
            else:
                label = "EH"

            structure.append(
                {
                    "time": current["time"],
                    "price": current["price"],
                    "label": label,
                }
            )

        # Higher Low / Lower Low
        for i in range(1, len(swing_lows)):

            previous = swing_lows[i - 1]
            current = swing_lows[i]

            if current["price"] > previous["price"]:
                label = "HL"
            elif current["price"] < previous["price"]:
                label = "LL"
            else:
                label = "EL"

            structure.append(
                {
                    "time": current["time"],
                    "price": current["price"],
                    "label": label,
                }
            )

        structure.sort(key=lambda x: x["time"])

        return structure

    # ==========================================
    # Return Last 4 Structure Points
    # ==========================================

    def get_last_structure(self):

        structure = self.classify_market_structure()

        if len(structure) < 4:
            return []

        return structure[-4:]

    # ==========================================
    # BOS Detection
    # ==========================================

    def detect_bos(self):

        highs = self.find_swing_highs()
        lows = self.find_swing_lows()

        if len(highs) == 0 or len(lows) == 0:
            return "NO BOS"

        current_price = float(self.df["Close"].iloc[-1])

        last_high = highs[-1]["price"]
        last_low = lows[-1]["price"]

        if current_price > last_high:
            return "BULLISH BOS"

        elif current_price < last_low:
            return "BEARISH BOS"

        return "NO BOS"

    # ==========================================
    # Placeholder Functions
    # ==========================================

    def detect_trend(self):
        pass

    def detect_choch(self):
        pass