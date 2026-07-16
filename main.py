from data.market_data import MarketData
from indicators.trend import TrendIndicator
from strategy.market_structure import MarketStructure

# ==========================================
# Download Market Data
# ==========================================

market = MarketData()
df = market.download()

# ==========================================
# Initialize Modules
# ==========================================

trend = TrendIndicator(df)
structure = MarketStructure(df)

# ==========================================
# Trend
# ==========================================

print("Trend :", trend.get_trend())

# ==========================================
# Last Swing High
# ==========================================

print("\nLast Swing High")
print(structure.find_swing_highs()[-1])

# ==========================================
# Last Swing Low
# ==========================================

print("\nLast Swing Low")
print(structure.find_swing_lows()[-1])

# ==========================================
# Last 10 Market Structure
# ==========================================

print("\nLast 10 Market Structure")

for item in structure.classify_market_structure()[-10:]:
    print(item)

# ==========================================
# BOS
# ==========================================

print("\nBOS")
print(structure.detect_bos())

# ==========================================
# Last 10 Merged Swings
# ==========================================

print("\nLast 10 Merged Swings")

merged = structure.merge_swings()

for item in merged[-10:]:
    print(item)

# ==========================================
# Last 4 Structure Points
# ==========================================

print("\nLast Structure")

last_structure = structure.get_last_structure()

for item in last_structure:
    print(item)