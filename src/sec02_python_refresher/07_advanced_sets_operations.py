# ----------------------------------------------------------------------
# ADVANCED SET OPERATIONS FOR INVENTORY
# ----------------------------------------------------------------------

# 1. Setup tag sets
master_allowed_tags = {"electronics", "appliances", "audio", "smart-home", "office"}

# Incoming product payloads we want to validate
incoming_product_a_tags = {"electronics", "audio", "gaming"}
incoming_product_b_tags = {"appliances", "smart-home"}

print("=== INVENTORY TAG AUDIT ENGINE ===")
print(f"Allowed Master Tags: {master_allowed_tags}\n")


# 2. DIFFERENCE (Finding invalid/unauthorized tags)
# What tags is Product A trying to use that are NOT in our allowed master list?
unauthorized_tags = incoming_product_a_tags.difference(master_allowed_tags)

print("--- 1. Difference (Unauthorized Tag Check) ---")
print(f"Product A Tags: {incoming_product_a_tags}")
if unauthorized_tags:
    print(f"⚠️ Warning! Unauthorized tags detected: {unauthorized_tags}")
else:
    print("✅ All tags are valid.")
print()


# 3. INTERSECTION (Finding shared tags)
# What categories does Product A share with our "office" and "audio" promo bundle?
promo_target_tags = {"audio", "office", "accessories"}
matching_promo_tags = incoming_product_a_tags.intersection(promo_target_tags)

print("--- 2. Intersection (Promo Match Check) ---")
print(f"Promo Targets:  {promo_target_tags}")
print(f"Product A Matches: {matching_promo_tags}")
print(f"Is eligible for promo? {len(matching_promo_tags) > 0}\n")


# 4. UNION (Merging catalogs)
# If we merge Product A and Product B tags, what is the combined unique tag profile?
combined_tags = incoming_product_a_tags.union(incoming_product_b_tags)

print("--- 3. Union (Catalog Merge) ---")
print(f"Combined Unique Tag Profile: {combined_tags}")