from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from transactions import ingest_csv, get_summary, transactions_db
from credit import (
    compute_financial_health,
    classify_behavior,
    debt_to_income,
    credit_limit,
    forecast_spending,
    loan_eligibility,
    statement_explainer,
    decision_log
)

app = FastAPI(title="FinGuard AI Backend")

# -----------------------------
# CORS (IMPORTANT for Streamlit)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "FinGuard AI running 🚀"}


# -----------------------------
# TRANSACTIONS
# -----------------------------
@app.post("/upload-transactions")
async def upload_transactions(file: UploadFile = File(...)):
    path = f"tx_{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    count = ingest_csv(path)

    return {"rows_ingested": count}


@app.get("/summary")
def summary():
    return get_summary()


@app.get("/live/transaction")
def live_transaction():
    import random
    import time

    sample = [
        {"amount": -12, "category": "Food", "merchant": "Starbucks"},
        {"amount": -45, "category": "Transport", "merchant": "Uber"},
        {"amount": -120, "category": "Shopping", "merchant": "Amazon"},
        {"amount": 2000, "category": "Income", "merchant": "Salary"},
    ]

    tx = random.choice(sample)
    tx["timestamp"] = time.time()

    transactions_db.append(tx)

    return tx


# -----------------------------
# FINANCIAL DECISION ENGINE
# -----------------------------
@app.get("/financial/advanced")
def financial_advanced():

    tx = transactions_db
    income = 5000

    health = compute_financial_health(tx)
    behavior = classify_behavior(tx)
    dti = debt_to_income(tx)

    credit = credit_limit(health["score"], income)

    forecast = forecast_spending(tx)

    loan = loan_eligibility(
        health["score"],
        income,
        dti["dti"]
    )

    explanation = statement_explainer(tx)

    log = decision_log(
        health["score"],
        dti["dti"],
        loan
    )

    return {
        "health": health,
        "behavior": behavior,
        "dti": dti,
        "credit_limit": credit,
        "forecast": forecast,
        "loan": loan,
        "explanation": explanation,
        "decision_log": log
    }


# -----------------------------
# ENTRY POINT (Hugging Face)
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)