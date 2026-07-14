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

print("\nLast Swing High")
print(highs[-1])

print("\nLast Swing Low")
print(lows[-1])