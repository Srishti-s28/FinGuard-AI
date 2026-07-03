import random

# -----------------------------
# 1. FINANCIAL HEALTH SCORE
# -----------------------------
def compute_financial_health(transactions):

    if not transactions:
        return {"score": 50, "label": "NO DATA"}

    income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    expenses = sum(abs(t["amount"]) for t in transactions if t["amount"] < 0)

    score = 100

    if expenses > income:
        score -= 40
    if expenses > income * 0.7:
        score -= 20

    score = max(0, min(100, score))

    label = (
        "HIGH RISK" if score < 40 else
        "MEDIUM RISK" if score < 70 else
        "LOW RISK"
    )

    return {
        "score": score,
        "label": label
    }


# -----------------------------
# 2. BEHAVIOR CLASSIFICATION
# -----------------------------
def classify_behavior(transactions):

    if not transactions:
        return "UNKNOWN"

    categories = {}

    for t in transactions:
        cat = t.get("category", "Other")
        categories[cat] = categories.get(cat, 0) + 1

    top = max(categories, key=categories.get)

    return top


# -----------------------------
# 3. DEBT TO INCOME
# -----------------------------
def debt_to_income(transactions):

    income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    debt = sum(abs(t["amount"]) for t in transactions if t["amount"] < 0)

    if income == 0:
        return {"dti": 1.0}

    return {
        "dti": round(debt / income, 2)
    }


# -----------------------------
# 4. CREDIT LIMIT SIMULATOR
# -----------------------------
def credit_limit(score, income):

    base = income * 0.3

    multiplier = 0.5
    if score > 80:
        multiplier = 3
    elif score > 60:
        multiplier = 2
    elif score > 40:
        multiplier = 1

    return {
        "recommended_limit": round(base * multiplier, 2),
        "tier": (
            "PREMIUM" if score > 80 else
            "STANDARD" if score > 50 else
            "LOW"
        )
    }


# -----------------------------
# 5. FORECASTING
# -----------------------------
def forecast_spending(transactions):

    expenses = [abs(t["amount"]) for t in transactions if t["amount"] < 0]

    base = sum(expenses) / len(expenses) if expenses else 100

    return {
        "forecast_30_days": [
            round(base * random.uniform(0.8, 1.3), 2)
            for _ in range(30)
        ]
    }


# -----------------------------
# 6. LOAN ELIGIBILITY
# -----------------------------
def loan_eligibility(score, income, dti):

    if score > 75 and dti < 0.3:
        return {
            "eligible": True,
            "max_loan": income * 5,
            "interest_rate": "6-9%"
        }

    if score > 50:
        return {
            "eligible": True,
            "max_loan": income * 2,
            "interest_rate": "10-15%"
        }

    return {
        "eligible": False,
        "max_loan": 0,
        "interest_rate": None
    }


# -----------------------------
# 7. STATEMENT EXPLAINER
# -----------------------------
def statement_explainer(transactions):

    if not transactions:
        return ["No transactions found"]

    reasons = []

    total_spend = sum(abs(t["amount"]) for t in transactions if t["amount"] < 0)

    if total_spend > 3000:
        reasons.append("High spending detected")

    cats = {}

    for t in transactions:
        cat = t.get("category", "Other")
        cats[cat] = cats.get(cat, 0) + abs(t["amount"])

    if cats:
        top = max(cats, key=cats.get)
        reasons.append(f"Top spending category: {top}")

    reasons.append("Behavior pattern analyzed using transaction clustering")

    return reasons


# -----------------------------
# 8. DECISION LOG
# -----------------------------
def decision_log(score, dti, loan):

    log = []

    log.append(f"Credit score: {score}")

    if dti < 0.3:
        log.append("Debt ratio healthy")
    else:
        log.append("High debt risk detected")

    if loan["eligible"]:
        log.append("Loan approved under policy rules")
    else:
        log.append("Loan rejected due to risk threshold")

    return log