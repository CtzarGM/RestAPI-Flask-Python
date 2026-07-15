# ----------------------------------------------------------------------
# DATABASE CONNECTION RETRY SIMULATOR (WHILE LOOPS)
# ----------------------------------------------------------------------
import time
import random

print("==================================================")
print("🔌 INVENTORY ENGINE - DATABASE CONNECTOR")
print("==================================================")

db_connected = False
attempt = 1
max_attempts = 5

# We loop until either we successfully connect, or we run out of allowed attempts
while not db_connected:
    print(f"Attempting connection to PostgreSQL (Attempt {attempt}/{max_attempts})...")
    
    # Simulate network latency
    time.sleep(0.5)
    
    # Simulate a 30% chance of a successful database handshake
    # random.random() returns a float between 0.0 and 1.0
    connection_success = random.random() < 0.3
    
    if connection_success:
        print("✅ Connection established! Syncing active catalog tables...\n")
        db_connected = True
        break  # Safely exit the loop
        
    print("❌ Connection failed: Database is starting up or network timed out.")
    
    # Increment attempts to avoid an infinite loop
    attempt += 1
    
    if attempt > max_attempts:
        print("\n🚨 CRITICAL SYSTEM ERROR: Maximum database connection attempts reached.")
        print("➡️ Action: Aborting process and notifying DevOps alerting pipeline.")
        break  # Exit the loop to prevent system hang
        
    print("Retrying in 1 second...\n")
    time.sleep(1)

print("==================================================")
print("System Status: Loop terminated safely. Execution resumed.")
print("==================================================")