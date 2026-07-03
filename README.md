FinGuard AI - Financial Risk & Credit Decisioning System

**Overview**

FinGuard AI is a financial analytics and decisioning system focused on three core banking capabilities:

1. Live market data monitoring
2. Credit risk analysis
3. Loan eligibility decision engine

The system simulates how banks evaluate customer financial health and determine creditworthiness using structured financial inputs and rule-based / model-driven logic.

**Core Modules**

Live Market Module
- Displays real-time financial/market-related indicators
- Simulated streaming data feed for financial context awareness
- Used to support risk evaluation decisions

Credit Analysis Engine
- Calculates financial risk score based on user financial behavior
- Evaluates creditworthiness using internal scoring logic
- Provides structured risk classification output

Loan Eligibility System
- Determines whether a user is eligible for a loan
- Uses credit score, income behavior, and risk thresholds
- Outputs decision: Approved / Rejected / Conditional


**System Architecture**

Frontend Layer
Streamlit-based interactive dashboard

Backend Layer
FastAPI services handling computation and decision logic

Core Logic Layer
- Credit scoring module
- Risk evaluation engine
- Loan decision rules

Data Layer
- Transaction and financial inputs
- Simulated or live market feeds

**Technology Stack**

- Frontend: Streamlit
- Backend: FastAPI
- Data Processing: Pandas
- Visualization: Plotly
- Language: Python

**System Capabilities**

- Live financial signal monitoring
- Credit score generation from financial inputs
- Risk classification (Low / Medium / High)
- Loan eligibility decisioning engine
- Explainable outputs for credit decisions

**Example Output**

Credit Score: 638  
Risk Level: Medium  
Loan Eligibility: Not Recommended  

Reasoning:
- Moderate income stability
- Elevated risk signals in financial behavior
- Credit threshold not satisfied for approval

**Running the Project**

Clone Repository
git clone https://github.com/Srishti-s28/FinGuard-AI.git
cd FinGuard-AI

Create Virtual Environment
python -m venv venv
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Run Backend
uvicorn backend.main:app --reload

Run Dashboard
streamlit run backend/dashboard.py

**Project Objective**

The objective of this system is to simulate core banking decision workflows including credit analysis, loan eligibility assessment, and financial signal monitoring.

The focus is on demonstrating financial logic, system design, and applied AI thinking in a fintech context.

**Business Relevance**

This project reflects real-world components used in:

- Retail banking credit decision systems
- Loan underwriting platforms
- Financial risk monitoring tools
- Fintech credit scoring engines

**Author**

Srishti
GitHub: https://github.com/Srishti-s28
