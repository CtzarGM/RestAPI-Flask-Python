# ----------------------------------------------------------------------
# MINI-APP: STORE VALUATION CALCULATOR
# ----------------------------------------------------------------------

print("=" * 50)
print("🏪 ENTERPRISE INVENTORY ENGINE - PORTAL v1.0")
print("=" * 50)

# 1. INPUT PHASE
store_name = input("Enter store/branch name: ").strip() or "General Warehouse"
currency = input("Enter currency symbol (e.g., $, €, ¥): ").strip() or "$"

print("\n--- Product Details ---")
product_a_name = input("Product A Name: ").strip() or "Unnamed Item A"
try:
    product_a_qty = int(input(f"Product A Qty in stock: "))
    product_a_price = float(input(f"Product A Unit Price ({currency}): "))
except ValueError:
    print("⚠️ Invalid numeric entry. Defaulting Product A to 0 units at 0.00.")
    product_a_qty, product_a_price = 0, 0.0

product_b_name = input("\nProduct B Name: ").strip() or "Unnamed Item B"
try:
    product_b_qty = int(input(f"Product B Qty in stock: "))
    product_b_price = float(input(f"Product B Unit Price ({currency}): "))
except ValueError:
    print("⚠️ Invalid numeric entry. Defaulting Product B to 0 units at 0.00.")
    product_b_qty, product_b_price = 0, 0.0


# 2. PROCESSING PHASE (Business Logic)
# Calculate valuations
val_a = product_a_qty * product_a_price
val_b = product_b_qty * product_b_price
total_valuation = val_a + val_b
total_items = product_a_qty + product_b_qty

# Prevent DivisionByZero if stock counts are both 0
avg_unit_price = (total_valuation / total_items) if total_items > 0 else 0.0


# 3. OUTPUT PHASE (Executive Dashboard)
print("\n" + "=" * 50)
print(f"📊 VALUATION REPORT: {store_name.upper()}")
print("=" * 50)
print(f"{'ITEM':<20} | {'QTY':<8} | {'UNIT PRICE':<10} | {'TOTAL':<10}")
print("-" * 50)
print(f"{product_a_name:<20} | {product_a_qty:<8} | {currency}{product_a_price:<9.2f} | {currency}{val_a:<9.2f}")
print(f"{product_b_name:<20} | {product_b_qty:<8} | {currency}{product_b_price:<9.2f} | {currency}{val_b:<9.2f}")
print("-" * 50)
print(f"Total Unique Stock Items:  {total_items}")
print(f"Average Unit Price:        {currency}{avg_unit_price:.2f}")
print(f"COMBINED PORTFOLIO VALUE:  {currency}{total_valuation:.2f}")
print("=" * 50)
print("Status: Report generated and cached. [Ready for DB pipeline]")
print("=" * 50 + "\n")