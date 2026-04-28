def calculate_profit(price, cost):
    margin = price - cost
    return margin

# --- Training Data ---
coffee_prices = [150, 200, 330]
unit_cost = 50

# STEP 1: Set Breakpoint on Line 10
for price in coffee_prices:
    profit = calculate_profit(price, unit_cost)
    print(f"Profit: {profit}")

