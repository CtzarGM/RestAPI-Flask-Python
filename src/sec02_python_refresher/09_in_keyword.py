# ----------------------------------------------------------------------
# MEMBERSHIP TESTING WITH THE 'IN' KEYWORD
# ----------------------------------------------------------------------

# Database states
recalled_skus = ["SKU-9988-XM", "SKU-4411-LQ", "SKU-1212-AB"]
active_campaign_tags = {"summer-sale", "clearance", "member-exclusive"}
store_name = "Tokyo flagship store"

print("=== MEMBERSHIP AUDIT UTILITY ===")

# 1. Checking lists (Searching for recalled SKUs)
target_sku = "SKU-4411-LQ"
is_recalled = target_sku in recalled_skus

print("--- 1. List Membership Check ---")
print(f"Target SKU:        {target_sku}")
print(f"Is SKU Recalled?   {is_recalled}")
if is_recalled:
    print("❌ ALERT: This product must be immediately removed from shelves!")
print()


# 2. Checking sets (O(1) lookups for campaign tag match)
incoming_tag = "summer-sale"
is_campaign_active = incoming_tag in active_campaign_tags

print("--- 2. Set Membership Check ---")
print(f"Incoming Tag:      {incoming_tag}")
print(f"Is Tag Active?     {is_campaign_active}")
print()


# 3. Checking substrings (String searching)
search_query = "tokyo"
match_found = search_query.lower() in store_name.lower()

print("--- 3. Substring Membership Check ---")
print(f"Search Query:      '{search_query}'")
print(f"Store Checked:     '{store_name}'")
print(f"Match Found?       {match_found}")
print("================================")