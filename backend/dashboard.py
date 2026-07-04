import streamlit as st
import requests
import time
import plotly.graph_objects as go

API = "https://srishti-2003-finguard-backend.hf.space"

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FinGuard Terminal",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- BLOOMBERG STYLE UI ----------------
st.markdown("""
<style>

body {
    background-color: #05070d;
    color: #d1d5db;
    font-family: "Segoe UI", monospace;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0b1220;
    border-right: 1px solid #1f2937;
}

/* Sidebar TEXT WHITE FIX */
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

[data-testid="stSidebar"] label {
    color: #ffffff !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

/* Sidebar hover effect */
[data-testid="stSidebar"] div:hover {
    background-color: rgba(56, 189, 248, 0.08);
    border-radius: 6px;
}

/* Main title glow */
h1 {
    color: #38bdf8;
    text-shadow: 0px 0px 12px rgba(56,189,248,0.4);
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: #0b1220;
    border: 1px solid #1f2937;
    padding: 12px;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background: #111827;
    color: #38bdf8;
    border: 1px solid #1f2937;
    border-radius: 6px;
}

.stButton > button:hover {
    background: #0f172a;
    border: 1px solid #38bdf8;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio("TERMINAL", [
    "LIVE MARKET",
    "RISK ANALYTICS",
    "CREDIT ENGINE"
])


# ================= LIVE MARKET =================
if menu == "LIVE MARKET":

    st.title("⚡ LIVE TRANSACTION STREAM")

    placeholder = st.empty()
    feed = []

    for _ in range(25):

        try:
            r = requests.get(f"{API}/live/transaction")
            tx = r.json()
        except:
            tx = {"merchant": "N/A", "category": "N/A", "amount": 0}

        feed.insert(0, tx)

        with placeholder.container():

            st.markdown("### Real-Time Banking Feed")

            for t in feed[:10]:
                col1, col2, col3 = st.columns([3, 2, 2])

                col1.write(f"🏦 {t['merchant']}")
                col2.write(t["category"])
                col3.write(f"£ {t['amount']}")

        time.sleep(0.6)


# ================= RISK ANALYTICS =================
elif menu == "RISK ANALYTICS":

    st.title("📊 RISK INTELLIGENCE ENGINE")

    try:
        data = requests.get(f"{API}/financial/advanced").json()
    except:
        data = {
            "health": {"score": 0, "label": "NO DATA"},
            "dti": {"dti": 0},
            "explanation": ["Backend not running"],
            "forecast": {"forecast_30_days": [0]*30}
        }

    health = data["health"]

    col1, col2, col3 = st.columns(3)

    col1.metric("CREDIT SCORE", health["score"])
    col2.metric("RISK STATUS", health["label"])
    col3.metric("DEBT RATIO", data["dti"]["dti"])

    st.markdown("---")

    st.markdown("### AI EXPLANATION LAYER")
    for r in data["explanation"]:
        st.write("•", r)

    st.markdown("---")

    st.markdown("### CASHFLOW SIMULATION")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=data["forecast"]["forecast_30_days"],
        mode="lines+markers",
        line=dict(color="#38bdf8", width=3)
    ))

    fig.update_layout(
        paper_bgcolor="#05070d",
        plot_bgcolor="#05070d",
        font=dict(color="#d1d5db"),
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)


# ================= CREDIT ENGINE =================
elif menu == "CREDIT ENGINE":

    st.title("🏦 CREDIT UNDERWRITING SYSTEM")

    try:
        data = requests.get(f"{API}/financial/advanced").json()
    except:
        data = {
            "credit_limit": {},
            "loan": {},
            "decision_log": ["Backend not running"]
        }

    st.success("Decision Engine Active")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### CREDIT LIMIT")
        st.json(data["credit_limit"])

    with col2:
        st.markdown("### LOAN DECISION")
        st.json(data["loan"])

    st.markdown("---")

    st.markdown("### DECISION LOG")

    for log in data["decision_log"]:
        st.write("•", log)