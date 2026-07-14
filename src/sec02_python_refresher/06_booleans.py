# ----------------------------------------------------------------------
# BOOLEAN LOGIC & COMPARISON DEMO
# ----------------------------------------------------------------------

# 1. Base State Definitions
stock_count = 5
safety_threshold = 10
has_write_permission = True
system_maintenance_mode = False

print("=== INVENTORY STATE ANALYSIS ===")

# 2. Simple Comparisons (Generating Booleans)
is_low_stock = stock_count < safety_threshold
is_out_of_stock = stock_count == 0

print(f"Stock Level:           {stock_count}")
print(f"Is Stock Low?          {is_low_stock}")
print(f"Is Stock Sold Out?     {is_out_of_stock}")


# 3. Combining Logic (Logical Operators: and, or, not)
# To execute an immediate order edit:
# - User must have write permission AND the system must NOT be in maintenance mode.
can_modify_inventory = has_write_permission and not system_maintenance_mode

print(f"User Can Write:        {has_write_permission}")
print(f"Maintenance Mode Active: {system_maintenance_mode}")
print(f"Can Modify Inventory?   {can_modify_inventory}")


# 4. Complex Security Check Example
# Let's verify if an emergency restock order can bypass maintenance.
# Bypass is True if: System is not in maintenance, OR (System is in maintenance BUT user is an admin)
is_admin = False
bypass_allowed = (not system_maintenance_mode) or is_admin

print(f"Bypass Restriction Allowed: {bypass_allowed}\n")


# 5. Value Equality (==) vs Memory Identity (is)
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("--- Comparison Operators: '==' vs 'is' ---")
print(f"list_a == list_b: {list_a == list_b} (True: values are identical)")
print(f"list_a is list_b: {list_a is list_b} (False: stored at different memory locations)")
print(f"list_a is list_c: {list_a is list_c} (True: reference the exact same memory object)")