from dataclasses import dataclass


@dataclass
class TradingConfig:

    # ==========================
    # MARKET
    # ==========================

    SYMBOL = "^NSEI"

    INTERVAL = "5m"

    PERIOD = "5d"

    # ==========================
    # EMA
    # ==========================

    EMA_FAST = 20

    EMA_SLOW = 50

    ATR_PERIOD = 14

    # ==========================
    # RISK
    # ==========================

    CAPITAL = 100000

    RISK_PER_TRADE = 0.02

    MAX_DAILY_LOSS = 5000

    LOT_SIZE = 65

    MAX_LOTS = 3

    # ==========================
    # AI
    # ==========================

    MIN_CONFIDENCE = 80

    # ==========================
    # REFRESH
    # ==========================

    REFRESH_SECONDS = 30


config = TradingConfig()