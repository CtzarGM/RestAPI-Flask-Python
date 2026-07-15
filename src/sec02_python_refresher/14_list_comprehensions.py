# ----------------------------------------------------------------------
# LIST COMPREHENSIONS FOR DATA FILTERING AND TRANSFORMATION
# ----------------------------------------------------------------------

# Raw database records
products = [
    {"sku": "sku-101a", "name": "Mechanical Keyboard", "price": 120.00, "stock": 4},
    {"sku": "sku-202b", "name": "Wireless Mouse", "price": 45.00, "stock": 18},
    {"sku": "sku-303c", "name": "UltraWide Monitor", "price": 350.00, "stock": 1},
    {"sku": "sku-404d", "name": "USB-C Hub", "price": 25.00, "stock": 0},
]

print("=== 1. Standard transformation ===")
# Traditional approach:
# upper_skus = []
# for p in products:
#     upper_skus.append(p["sku"].upper())

# List Comprehension approach:
upper_skus = [p["sku"].upper() for p in products]
print(f"Sanitized Upper SKUs: {upper_skus}\n")


print("=== 2. Filtering (Sieving datasets) ===")
# Extract only products that are out of stock or low (stock < 5)
low_stock_items = [p for p in products if p["stock"] < 5]
print("Low Stock Alerts:")
for item in low_stock_items:
    print(f" -> {item['name']} (Stock remaining: {item['stock']})")
print()


print("=== 3. Mapping with Complex Inline Conditionals ===")
# If we want an 'else' block inside our expression, we move the conditional to the front:
# [value_if_true if condition else value_if_false for item in iterable]

# Label products as 'On Sale!' if price is greater than 100, otherwise label 'Standard'
price_labels = [f"{p['name']}: Sale!" if p["price"] > 100.00 else f"{p['name']}: Standard" for p in products]
print("Price Tier Categories:")
for label in price_labels:
    print(f" * {label}")