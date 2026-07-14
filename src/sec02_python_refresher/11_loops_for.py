# ----------------------------------------------------------------------
# BATCH INVENTORY VALUE REPORTING (FOR LOOPS)
# ----------------------------------------------------------------------

# Simulated database records: A list of dictionaries representing products
inventory_batch = [
    {"name": "Mechanical Keyboard", "price": 120.00, "stock": 15},
    {"name": "Wireless Mouse", "price": 45.50, "stock": 42},
    {"name": "UltraWide Monitor", "price": 350.00, "stock": 8},
    {"name": "USB-C Hub Adapter", "price": 25.00, "stock": 0},  # Out of stock
]

print("==================================================")
print("📊 BATCH INVENTORY VALUATION RUN")
print("==================================================")

total_warehouse_value = 0.0
total_item_count = 0

# 1. Iterating through a list of dictionaries
for product in inventory_batch:
    name = product["name"]
    price = product["price"]
    stock = product["stock"]
    
    # Calculate item valuation
    item_valuation = price * stock
    total_warehouse_value += item_valuation
    total_item_count += stock
    
    # Check if we need to alert about out of stock items
    if stock == 0:
        status = "⚠️ OUT OF STOCK"
    else:
        status = f"Stock: {stock}"
        
    print(f"Product: {name:<20} | {status:<15} | Value: ${item_valuation:.2f}")

print("-" * 50)
print(f"Total Combined Stock Quantity:  {total_item_count} units")
print(f"Total Warehouse Asset Value:   ${total_warehouse_value:.2f}")
print("==================================================\n")


# 2. Iterating through a dictionary's key-value pairs
print("=== WAREHOUSE DEPARTMENT STORAGE METRICS ===")
department_capacities = {
    "Aisle A (Electronics)": "85% Capacity",
    "Aisle B (Accessories)": "40% Capacity",
    "Aisle C (Monitors)":    "92% Capacity (HIGH)"
}

# Using .items() allows us to destructure key and value directly in the loop
for location, status in department_capacities.items():
    print(f"📍 {location}: {status}")