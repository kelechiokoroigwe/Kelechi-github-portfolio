import json
import random
import time
from datetime import datetime

locations = ["US", "UK", "NG", "DE", "FR"]
devices = ["mobile", "desktop", "tablet"]


def generate_transaction():
    """
    Generate a simulated transaction record.

    Returns:
        dict: A dictionary containing transaction details.
    """
    txn = {
        "transaction_id": random.randint(100000, 999999),
        "user_id": random.randint(1000, 9999),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "location": random.choice(locations),
        "device": random.choice(devices),
        "timestamp": datetime.utcnow().isoformat(),
    }
    return txn


while True:
    transaction = generate_transaction()
    print(json.dumps(transaction, indent=2))
    time.sleep(2)  # Simulate delay between transactions