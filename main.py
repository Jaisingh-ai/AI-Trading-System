from data.market_data import MarketData
from indicators.trend import TrendIndicator
from strategy.market_structure import MarketStructure

market = MarketData()

df = market.download()

trend = TrendIndicator(df)

print("Trend :", trend.get_trend())

structure = MarketStructure(df)

highs = structure.find_swing_highs()

print("\nSwing High Count :", len(highs))

print("Last 10 Swing High Index :", highs[-10:])