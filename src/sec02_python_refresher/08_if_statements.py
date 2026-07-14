#!/usr/bin/env python3
# ----------------------------------------------------------------------
# ORDER PROCESSING DECISION TREE
# ----------------------------------------------------------------------

# Current System State
product_stock = 15
order_quantity = 20
warehouse_online = True
is_vip_customer = True

print("=== AUTOMATED ORDER FULFILLMENT SYSTEM ===")

# 1. Base check: Is the fulfillment center accepting orders?
if not warehouse_online:
    print("❌ Order Rejected: Warehouse is currently offline for maintenance.")

# 2. Evaluate inventory availability and backorder routing
else:
    print(f"Incoming Order Quantity: {order_quantity} units")
    print(f"Available Stock Level:   {product_stock} units")
    
    if order_quantity <= product_stock:
        print("✅ Order Approved: Sufficient stock available for immediate dispatch.")
        product_stock -= order_quantity  # Simulate stock deduction
        
    elif is_vip_customer:
        print("⚠️ Order Held: Insufficient stock, but VIP status detected.")
        print("➡️ Action: Splitting order into immediate partial shipment + prioritised backorder.")
        product_stock = 0
        
    else:
        print("❌ Order Rejected: Insufficient stock. Backordering is disabled for standard accounts.")

print("==========================================")