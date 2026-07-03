import pandas as pd
import numpy as np

def generate_mock_portfolio():
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)

    return pd.DataFrame({
        "date": dates,
        "balance": np.cumsum(np.random.randint(-500, 1500, 30)) + 50000
    })


def generate_spending():
    return pd.DataFrame({
        "category": ["Food", "Rent", "Travel", "Shopping", "Bills"],
        "amount": [1200, 2500, 800, 1500, 600]
    })