# ----------------------------------------------------------------------
# COMPLEX FLOW CONTROL: INVENTORY AUDITING AND REORDER ENGINE
# ----------------------------------------------------------------------

# Current store inventory records
active_catalog = [
    {"sku": "SKU-101", "name": "Mechanical Keyboard", "stock": 4, "reorder_point": 10, "hazardous": False},
    {"sku": "SKU-202", "name": "Lithium Battery Pack", "stock": 1, "reorder_point": 5, "hazardous": True},
    {"sku": "SKU-303", "name": "Ergonomic Office Chair", "stock": 12, "reorder_point": 5, "hazardous": False},
    {"sku": "SKU-404", "name": "Liquid Cleaning Agent", "stock": 0, "reorder_point": 3, "hazardous": True},
    {"sku": "SKU-505", "name": "USB-C Cable 1m", "stock": 50, "reorder_point": 15, "hazardous": False},
]

print("==================================================")
print("🏭 AUTOMATED DISPATCH & SAFETY REORDER SYSTEM")
print("==================================================")

reorder_queue = []
hazardous_alerts = []

for product in active_catalog:
    sku = product["sku"]
    name = product["name"]
    stock = product["stock"]
    reorder_point = product["reorder_point"]
    is_hazardous = product["hazardous"]
    
    # 1. Skip items that are extremely overstocked to save processing overhead
    if stock > reorder_point * 3:
        print(f"ℹ️ {sku:<8} | {name:<24} | Overstock detected ({stock} units). Skipping audit.")
        continue  # Skip to the next product in the loop
        
    # 2. Check if the item has fallen below its safety reorder threshold
    if stock <= reorder_point:
        deficit = reorder_point - stock
        reorder_qty = deficit * 2  # Replenishment policy: order twice the deficit
        
        print(f"⚠️ {sku:<8} | {name:<24} | Low stock ({stock}/{reorder_point}). Generating reorder of {reorder_qty} units.")
        reorder_queue.append({"sku": sku, "qty": reorder_qty})
        
        # 3. Handle a nested condition: check safety constraints for hazardous items
        if is_hazardous:
            hazardous_alerts.append(sku)
            if stock == 0:
                print(f"🚨 CRITICAL: Hazardous item {sku} is completely out of stock! Immediate hazard escalation triggered.")
    else:
        print(f"✅ {sku:<8} | {name:<24} | Stock level healthy ({stock} units).")

print("-" * 50)
print("=== ENGINE SUMMARY ===")
print(f"Total standard reorders queued: {len(reorder_queue)}")
if hazardous_alerts:
    print(f"⚠️ High-Priority Hazmat Safety Audits Required: {hazardous_alerts}")
print("==================================================")