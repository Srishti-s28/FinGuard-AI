import pandas as pd
import random
import time

transactions_db = []


def ingest_csv(file_path):
    df = pd.read_csv(file_path)

    global transactions_db
    transactions_db.extend(df.to_dict(orient="records"))

    return len(df)


def get_summary():
    if not transactions_db:
        return {
            "total_transactions": 0,
            "total_spent": 0,
            "categories": {}
        }

    df = pd.DataFrame(transactions_db)

    return {
        "total_transactions": len(df),
        "total_spent": float(df.get("amount", pd.Series([0])).sum()),
        "categories": df.get("category", pd.Series([])).value_counts().to_dict()
    }


def add_fake_transaction():
    sample = [
        {"amount": -12, "category": "Coffee", "merchant": "Starbucks"},
        {"amount": -45, "category": "Food", "merchant": "McDonalds"},
        {"amount": -120, "category": "Shopping", "merchant": "Amazon"},
        {"amount": 2000, "category": "Income", "merchant": "Salary"},
    ]

    tx = random.choice(sample)
    tx["timestamp"] = time.time()

    transactions_db.append(tx)

    return tx