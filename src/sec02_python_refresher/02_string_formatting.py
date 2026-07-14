# ----------------------------------------------------------------------
# SERVER LOG ENGINE (String Formatting)
# ----------------------------------------------------------------------

# Raw data retrieved from our mock inventory database
product_name = "Premium Wireless Mouse"
stock_count = 12
unit_price = 89.9543  # Database float with high precision
is_active = True

print("=== SYSTEM LOG GENERATOR ===")

# 1. Using .format() for templates
# This is great for reusable alert layouts
alert_template = "[ALERT] - System Status: {status}. Active Items: {count}."
print(alert_template.format(status="ONLINE" if is_active else "OFFLINE", count=stock_count))


# 2. Using F-Strings for precise output
# We will use formatting specs:
# - :>20 pads the name to be right-aligned with 20 spaces
# - :.2f rounds the unit price to exactly 2 decimal places
# - Inline math calculates the total valuation on the fly
print("\n--- Current Inventory Record ---")
print(f"Product:      {product_name:>25}")
print(f"Stock Level:  {stock_count:>25}")
print(f"Unit Price:   ${unit_price:>24.2f}")
print(f"Total Value:  ${(stock_count * unit_price):>24.2f}")
print("-" * 38)


# 3. Dynamic formatting in lists
tags = ["electronics", "peripherals", "ergonomic"]
print(f"Tags:         [{', '.join(tags)}]")
print("================================\n")