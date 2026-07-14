# ----------------------------------------------------------------------
# PYTHON COLLECTIONS DEMO
# ----------------------------------------------------------------------

# 1. LISTS (Ordered, mutable, allows duplicates)
print("=== 1. Lists (Active Store Catalog) ===")
active_catalog = ["SKU-A", "SKU-B", "SKU-C"]
print(f"Original Catalog: {active_catalog}")

# We can append and modify items easily
active_catalog.append("SKU-D")
active_catalog.append("SKU-A")  # Duplicates are allowed
print(f"Updated Catalog:  {active_catalog}")
print(f"First Item:       {active_catalog[0]}")  # Ordered indexing works
print(f"Last Item:        {active_catalog[-1]}\n")


# 2. TUPLES (Ordered, immutable, allows duplicates)
print("=== 2. Tuples (Fixed Warehouse Location) ===")
# Coordinates of our main warehouse: (Latitude, Longitude)
warehouse_location = (40.7128, -74.0060)
print(f"Warehouse Coordinates: {warehouse_location}")
print(f"Latitude: {warehouse_location[0]}")

# Trying to modify a tuple will raise an error!
try:
    # warehouse_location[0] = 34.0522  # Uncommenting this throws a TypeError
    print("Coordinates are locked and secure (tuples cannot be mutated).")
except TypeError:
    print("❌ Error: You cannot modify a tuple!")
print()


# 3. SETS (Unordered, mutable, strictly unique)
print("=== 3. Sets (Unique Product Category Tags) ===")
active_tags = {"appliances", "kitchen", "smart-home"}
print(f"Initial Tags:     {active_tags}")

# Adding a duplicate tag does nothing
active_tags.add("kitchen")
active_tags.add("clearance")
print(f"After additions:  {active_tags} (Notice 'kitchen' is not duplicated!)")

# Quick membership testing (highly optimized in sets)
has_clearance = "clearance" in active_tags
print(f"Is 'clearance' tag present? {has_clearance}")