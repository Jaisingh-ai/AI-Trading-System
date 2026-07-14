"""
===========================================
AI Trading System
Module: Market Data Engine

Description:
Downloads, validates and processes market data.
===========================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd
import yfinance as yf

from config.settings import config
from utils.logger import get_logger

logger = get_logger(__name__)


@dataclass
class MarketSnapshot:
    symbol: str
    current_price: float
    previous_high: float
    previous_low: float
    previous_close: float
    today_open: float
    gap_percent: float


class MarketData:

    def __init__(self, symbol: Optional[str] = None):
        self.symbol = symbol or config.SYMBOL
        self.df: Optional[pd.DataFrame] = None

    def download(self) -> pd.DataFrame:

        logger.info(f"Downloading data for {self.symbol}")

        df = yf.download(
            self.symbol,
            period=config.PERIOD,
            interval=config.INTERVAL,
            progress=False,
            auto_adjust=True
        )

        # Remove MultiIndex if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if df.empty:
            raise ValueError("No market data received.")

        self.df = df

        return df

    def validate_data(self) -> bool:

        if self.df is None:
            logger.error("No data downloaded.")
            return False

        required_columns = [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]

        for column in required_columns:

            if column not in self.df.columns:
                logger.error(f"Missing column : {column}")
                return False

        logger.info("Market data validated successfully.")

        return True

    def get_current_price(self) -> float:

        if self.df is None:
            raise ValueError("Download data first.")

        return float(self.df["Close"].iloc[-1])

    def get_previous_day(self) -> dict:

        if self.df is None:
            raise ValueError("Download data first.")

        unique_days = sorted(self.df.index.normalize().unique())

        if len(unique_days) < 2:
            raise ValueError("Not enough previous day data.")

        previous_day = unique_days[-2]

        previous_df = self.df[
            self.df.index.normalize() == previous_day
        ]

        return {
            "high": float(previous_df["High"].max()),
            "low": float(previous_df["Low"].min()),
            "close": float(previous_df["Close"].iloc[-1])
        }

    def calculate_gap(self) -> float:

        if self.df is None:
            raise ValueError("Download data first.")

        previous = self.get_previous_day()

        today = self.df[
            self.df.index.normalize() == self.df.index.normalize()[-1]
        ]

        today_open = float(today["Open"].iloc[0])

        gap = (
            (today_open - previous["close"])
            / previous["close"]
        ) * 100

        return round(gap, 2)

    def get_snapshot(self) -> MarketSnapshot:

        previous = self.get_previous_day()

        today = self.df[
            self.df.index.normalize() == self.df.index.normalize()[-1]
        ]

        return MarketSnapshot(
            symbol=self.symbol,
            current_price=self.get_current_price(),
            previous_high=previous["high"],
            previous_low=previous["low"],
            previous_close=previous["close"],
            today_open=float(today["Open"].iloc[0]),
            gap_percent=self.calculate_gap()
        )