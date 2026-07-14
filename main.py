from data.market_data import MarketData

market = MarketData()

market.download()

print("Validation :", market.validate_data())

snapshot = market.get_snapshot()

print("\n========== MARKET SNAPSHOT ==========")
print("Symbol         :", snapshot.symbol)
print("Current Price  :", snapshot.current_price)
print("Today's Open   :", snapshot.today_open)
print("Previous High  :", snapshot.previous_high)
print("Previous Low   :", snapshot.previous_low)
print("Previous Close :", snapshot.previous_close)
print("Gap %          :", snapshot.gap_percent)