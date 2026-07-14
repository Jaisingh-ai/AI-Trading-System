from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TradingConfig:
    """
    Central configuration for the AI Trading System.
    """

    # ==========================
    # Market
    # ==========================
    SYMBOL: str = "^NSEI"
    PERIOD: str = "5d"
    INTERVAL: str = "5m"

    # ==========================
    # Indicators
    # ==========================
    EMA_FAST: int = 20
    EMA_SLOW: int = 50
    ATR_PERIOD: int = 14

    # ==========================
    # Trading
    # ==========================
    CAPITAL: float = 100000.0
    LOT_SIZE: int = 65
    MAX_LOTS: int = 3

    RISK_PER_TRADE: float = 0.02
    MAX_DAILY_LOSS: float = 5000.0

    # ==========================
    # AI
    # ==========================
    MIN_CONFIDENCE: int = 80

    # ==========================
    # Refresh
    # ==========================
    REFRESH_SECONDS: int = 30

    # ==========================
    # Directories
    # ==========================
    LOG_DIR: Path = Path("logs")
    DATA_DIR: Path = Path("data")


config = TradingConfig()