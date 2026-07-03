# fraud.py

def detect_fraud(transactions):

    alerts = []

    for t in transactions:

        amount = t.get("amount", 0)
        category = t.get("category", "")

        # RULE 1: unusually high transaction
        if amount > 5000:
            alerts.append("🚨 High-value transaction detected")

        # RULE 2: risky categories
        if category in ["crypto", "gambling", "betting"]:
            alerts.append("⚠️ High-risk category transaction")

        # RULE 3: rapid spending pattern (simple heuristic)
        if amount > 2000 and category == "shopping":
            alerts.append("⚠️ Potential impulsive spending pattern")

    return alerts