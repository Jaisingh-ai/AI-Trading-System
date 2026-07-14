from data.market_data import MarketData
from indicators.trend import TrendIndicator
from strategy.market_structure import MarketStructure

market = MarketData()

df = market.download()

trend = TrendIndicator(df)

structure = MarketStructure(df)

highs = structure.find_swing_highs()
lows = structure.find_swing_lows()

print("Trend :", trend.get_trend())

print("\nSwing High Count :", len(highs))
print("Last 10 Swing High :", highs[-10:])

print("\nSwing Low Count :", len(lows))
print("Last 10 Swing Low :", lows[-10:])