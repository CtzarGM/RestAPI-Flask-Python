# ----------------------------------------------------------------------
# CLI PRODUCT INTAKE TOOL
# ----------------------------------------------------------------------
print("==========================================")
print("📦 ENTERPRISE INVENTORY INTAKE WIZARD")
print("==========================================\n")

# 1. Capture basic string inputs
product_name = input("Enter product name: ").strip()
category = input("Enter product category: ").strip()

# 2. Capture numeric values with explicit type casting
# We use try/except blocks to prevent crashes if the user types invalid numbers
try:
    raw_price = input("Enter unit price (USD): ")
    price = float(raw_price)
except ValueError:
    print("\n❌ Error: Invalid price format. Setting default price to $0.00")
    price = 0.0

try:
    raw_stock = input("Enter initial stock quantity: ")
    stock = int(raw_stock)
except ValueError:
    print("\n❌ Error: Invalid stock quantity. Setting default stock to 0")
    stock = 0

# 3. Calculate total potential value
total_valuation = price * stock

# 4. Display the formatted database entry confirmation
print("\n" + "="*42)
print("📝 STAGED DATABASE RECORD CREATION")
print("="*42)
print(f"Product:      {product_name}")
print(f"Category:     {category}")
print(f"Unit Price:   ${price:.2f}")
print(f"Stock Qty:    {stock}")
print(f"Total Value:  ${total_valuation:.2f}")
print("="*42)
print("✅ Record successfully validated for database serialization!\n")