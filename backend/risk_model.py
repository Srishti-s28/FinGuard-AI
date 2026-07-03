import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([
    [50000, 20000, 5],
    [80000, 10000, 1],
    [30000, 25000, 10],
    [100000, 20000, 0]
])

y = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

def predict_risk(income, expenses, late_payments):
    pred = model.predict([[income, expenses, late_payments]])[0]
    prob = model.predict_proba([[income, expenses, late_payments]])[0][1]

    return {
        "risk": "HIGH" if pred == 1 else "LOW",
        "probability": float(prob)
    }