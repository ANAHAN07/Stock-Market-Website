import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta



API_URL = "https://api.exchangerate-api.com/v4/latest/"     # API KEY for currency real time update.



def fetch_exchange_rate(base_currency, target_currency):        # Taking real time update of currency.
    response = requests.get(API_URL + base_currency)
    data = response.json()
    return data["rates"].get(target_currency, None)


def fetch_historical_rates(base_currency, target_currency, days=30):       # Taking past exchange rates for graph
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    
    dates = pd.date_range(start=start_date, end=end_date).tolist()
    rates = [fetch_exchange_rate(base_currency, target_currency) or 1 for _ in dates]

    df = pd.DataFrame({"Date": dates, "Exchange Rate": rates})
    
    # Get lowest and highest value
    lowest_value = df["Exchange Rate"].min()
    highest_value = df["Exchange Rate"].max()
    lowest_date = df.loc[df["Exchange Rate"] == lowest_value, "Date"].values[0]
    highest_date = df.loc[df["Exchange Rate"] == highest_value, "Date"].values[0]

    return df, lowest_value, lowest_date, highest_value, highest_date


def currency_exchange_page():
    st.title("💱 Currency Exchange")            # Currency exchange box


    currencies = ["USD", "EUR", "BDT", "INR", "CNY", "AED", "KWD", "GBP", "CAD"]        # Select currencies
    currency_from = st.selectbox("From Currency", currencies, index=0)
    currency_to = st.selectbox("To Currency", currencies, index=2)
    amount = st.number_input("Amount", min_value=0.0, value=1.0)


    exchange_rate = fetch_exchange_rate(currency_from, currency_to)     # Exchange rate


    if exchange_rate:
        converted_value = amount * exchange_rate
        st.success(f"💲 {amount} {currency_from} = {converted_value:.2f} {currency_to} (Rate: {exchange_rate:.4f})")


        df, lowest_value, lowest_date, highest_value, highest_date = fetch_historical_rates(currency_from, currency_to)     # Historical graph
        

        # Display additional info
        st.write(f"📌 **Current Value**: {exchange_rate:.4f}")
        st.write(f"🔻 **Lowest Value**: {lowest_value:.4f} on {lowest_date}")
        st.write(f"🔺 **Highest Value**: {highest_value:.4f} on {highest_date}")


        fig = px.line(df, x="Date", y="Exchange Rate", title=f"Exchange Rate Trend ({currency_from} to {currency_to})")     # trend graph
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("❌ Unable to fetch exchange rate. Try again later.")



if __name__ == "__main__":
    currency_exchange_page()