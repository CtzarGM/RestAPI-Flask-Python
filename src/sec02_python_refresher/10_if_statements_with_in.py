# ----------------------------------------------------------------------
# API REQUEST VALIDATOR (IF + IN)
# ----------------------------------------------------------------------

# 1. API Configuration / Validation Rules
REQUIRED_FIELDS = {"name", "price", "stock"}
APPROVED_CURRENCIES = {"USD", "EUR", "JPY"}
BLACKLISTED_WORDS = {"spam", "test-product", "fake"}

# 2. Simulated Incoming Payloads (Incoming JSON)
incoming_payload = {
    "name": "Mechanical Keyboard (test-product)",
    "price": 129.99,
    "stock": 45,
    "currency": "CAD"
}

print("=== INCOMING API PAYLOAD AUDIT ===")

# Check 1: Ensure all required structural keys are present
# We check if any required key is missing from the payload dictionary keys
missing_fields = []
for field in REQUIRED_FIELDS:
    if field not in incoming_payload:
        missing_fields.append(field)

if len(missing_fields) > 0:
    print(f"❌ API Schema Error: Missing required fields: {missing_fields}")
else:
    print("✅ Schema Check: All required structural fields present.")


# Check 2: Validate the currency choice
# In Python dictionaries, checking 'in' directly checks keys.
# We explicitly fetch the 'currency' key if it exists, defaulting to 'USD' if not.
currency_used = incoming_payload.get("currency", "USD")

if currency_used not in APPROVED_CURRENCIES:
    print(f"❌ Validation Warning: Currency '{currency_used}' is not supported. Supported currencies: {APPROVED_CURRENCIES}")
else:
    print(f"✅ Currency Check: '{currency_used}' is approved.")


# Check 3: Content Sanitization (Searching for blacklisted terms in the product name)
product_name = incoming_payload.get("name", "").lower()
has_violation = False

# We iterate through our blacklisted words to see if any exist in our product name
for word in BLACKLISTED_WORDS:
    if word in product_name:
        print(f"❌ Content Policy Violation: Product name contains restricted term '{word}'!")
        has_violation = True
        break

if not has_violation:
    print("✅ Content Check: Product name is fully cleared.")

print("==================================")