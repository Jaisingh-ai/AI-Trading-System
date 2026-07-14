from data.market_data import MarketData
from indicators.trend import TrendIndicator

market = MarketData()

df = market.download()

trend = TrendIndicator(df)

print("Trend :", trend.get_trend())