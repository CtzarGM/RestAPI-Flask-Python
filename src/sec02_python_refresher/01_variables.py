# ----------------------------------------------------------------------
# 1. IMMUTABLE REFERENCES (Strings)
# ----------------------------------------------------------------------
print("--- 1. Immutable Reference Test (SKU Strings) ---")

sku_a = "SKU-9988-XM"
sku_b = sku_a  # Both variables point to the exact same string object in memory

print(f"sku_a: {sku_a} | Memory ID: {id(sku_a)}")
print(f"sku_b: {sku_b} | Memory ID: {id(sku_b)}")
print(f"Point to same object? {sku_a is sku_b}\n")

# Reassigning sku_a creates a *new* object. It does not overwrite sku_b's data.
sku_a = "SKU-1122-NY"
print("--> sku_a modified/reassigned:")
print(f"sku_a: {sku_a} | Memory ID: {id(sku_a)}")
print(f"sku_b: {sku_b} | Memory ID: {id(sku_b)}")
print(f"Point to same object now? {sku_a is sku_b}\n")


# ----------------------------------------------------------------------
# 2. MUTABLE REFERENCES (Lists)
# ----------------------------------------------------------------------
print("--- 2. Mutable Reference Test (Product Tags) ---")

tags_store_one = ["electronics", "smart-home"]
tags_store_two = tags_store_one  # Both point to the exact same list object

print(f"tags_store_one: {tags_store_one} | Memory ID: {id(tags_store_one)}")
print(f"tags_store_two: {tags_store_two} | Memory ID: {id(tags_store_two)}")
print(f"Point to same object? {tags_store_one is tags_store_two}\n")

# Modifying the list in-place via one pointer affects both!
print("--> Appending a tag to 'tags_store_one'...")
tags_store_one.append("sale")

print(f"tags_store_one: {tags_store_one} | Memory ID: {id(tags_store_one)}")
print(f"tags_store_two: {tags_store_two} | Memory ID: {id(tags_store_two)}")
print(f"Did both change? Yes, because they reference the same list.")