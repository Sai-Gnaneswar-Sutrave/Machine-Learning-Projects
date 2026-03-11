import streamlit as st
import requests
from datetime import datetime

API_URL = "http://localhost:8000/predict"


def main():
    """
    Streamlit UI for Bank Transfer Anomaly Detection
    """

    st.set_page_config(page_title="Bank Transfer Anomaly Detection", layout="wide")

    st.title("🏦 Bank Transfer Anomaly Detection")
    st.write("Enter transaction details to detect whether the transaction is anomalous.")

    col1, col2 = st.columns(2)

    with col1:
        account_balance = st.number_input("Account Balance", min_value=0.0, step=0.01)
        customer_age = st.number_input("Customer Age", min_value=18, max_value=100, step=1)
        login_attempts = st.number_input("Login Attempts", min_value=0, step=1)
        transaction_date = st.date_input("Transaction Date")
        channel = st.selectbox("Channel", ["ATM", "Branch", "Online"])
        location = st.text_input("Location")

    with col2:
        transaction_amount = st.number_input("Transaction Amount", min_value=0.0, step=0.01)
        transaction_duration = st.number_input("Transaction Duration (seconds)", min_value=0.0, step=0.01)
        recent_transaction_date = st.date_input("Most Recent Transaction Date")
        customer_occupation = st.selectbox(
            "Customer Occupation",
            ["Doctor", "Engineer", "Retired", "Student"]
        )
        transaction_type = st.selectbox("Transaction Type", ["Credit", "Debit"])

    st.divider()

    if st.button("Predict Transaction Risk"):

        user_input = {
            "accountBalance": account_balance,
            "customerAge": customer_age,
            "loginAttempts": login_attempts,
            "transactionAmount": transaction_amount,
            "transactionDuration": transaction_duration,
            "transactionDate": transaction_date.isoformat(),
            "recentTransactionDate": recent_transaction_date.isoformat(),
            "channel": channel,
            "customerOccupation": customer_occupation,
            "location": location,
            "transactionType": transaction_type
        }

        with st.spinner("Analyzing transaction..."):
            response = requests.post(API_URL, json=user_input)
            if response.status_code == 200:
                result = response.json()
                score = result["anomaly_score"]
                st.subheader("Prediction Result")
                col1, col2 = st.columns(2)
                col1.metric("Prediction", result["prediction"])
                col2.metric("Anomaly Score", f"{score:.4f}")

                st.divider()

                if score < -0.1:
                    st.error(f"🚨 High Risk Transaction Detected\n\nScore: {score:.4f}")
                elif score < 0:
                    st.warning(f"⚠️ Suspicious Transaction\n\nScore: {score:.4f}")
                else:
                    st.success(f"✅ Transaction appears Normal\n\nScore: {score:.4f}")
            else:
                st.error(response.json())


if __name__ == "__main__":
    main()