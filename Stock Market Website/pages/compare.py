import streamlit as st
import yfinance as yf
import pandas as pd



# Defining a mapping of stock exchanges to valid stock tickers
stock_mapping = {
    "New York Stock Exchange": "AAPL",  # Apple Inc.
    "Nasdaq Stock Market": "GOOGL",  # Alphabet (Google)
    "London Stock Exchange": "HSBA.L",  # HSBC Holdings
    "Tokyo Stock Exchange": "6758.T",  # Sony Corporation
    "Shanghai Stock Exchange": "601398.SS",  # Industrial & Commercial Bank of China
    "Hong Kong Stock Exchange": "0700.HK",  # Tencent Holdings
    "Toronto Stock Exchange": "RY.TO",  # Royal Bank of Canada
    "Australian Securities Exchange": "BHP.AX",  # BHP Group
    "Bombay Stock Exchange": "RELIANCE.BO",  # Reliance Industries
    "National Stock Exchange of India": "TCS.NS",  # Tata Consultancy Services
    "Deutsche Börse (Frankfurt Stock Exchange)": "BMW.DE",  # BMW AG
    "SIX Swiss Exchange": "NESN.SW",  # Nestlé S.A.
    "Korea Exchange": "005930.KQ",  # Samsung Electronics
    "Singapore Exchange": "D05.SI",  # DBS Bank
    "Johannesburg Stock Exchange": "NPN.JO",  # Naspers
    "São Paulo Stock Exchange": "VALE3.SA",  # Vale S.A.
    "Brent Crude Oil": "BZ=F",  # Brent Crude Oil Futures
    "West Texas Intermediate Oil": "CL=F",  # WTI Crude Oil Futures
    "BHP Group Limited": "BHP", # BHP Group Limited
    "Rio Tinto Group": "RIO",   # Rio Tinto Group
    "Vale S.A.": "VALE"     # Vale S.A
}


# Function to get stock data
def get_stock_data(ticker):
    if not ticker:
        return None  # Handle missing tickers
    stock = yf.Ticker(ticker)
    data = stock.history(period="1wk")  # Fetch the data for the past week
    return data


def compare_page():
    st.title("Compare Shares")

    # Select two shares to compare
    stock_names = list(stock_mapping.keys())
    
    share1_name = st.selectbox("Select First Stock Exchange", stock_names)
    share2_name = st.selectbox("Select Second Stock Exchange", stock_names)


    # Convert selected exchanges to valid stock tickers
    share1 = stock_mapping.get(share1_name)
    share2 = stock_mapping.get(share2_name)


    # Fetch stock data
    data1 = get_stock_data(share1)
    data2 = get_stock_data(share2)


    # Handle missing data
    if data1 is None or data1.empty or data2 is None or data2.empty:
        st.error("No data available for one or both of the selected stocks. Please try again later.")
        return


    # Showing stock comparison
    st.subheader("Comparison Results")


    # Displaying details about both stocks
    st.write(f"**Company 1: {share1_name} ({share1})**")
    st.write(f"**Current Price:** {data1['Close'].iloc[-1]}")
    st.write(f"**Week High:** {data1['High'].max()}")
    st.write(f"**Week Low:** {data1['Low'].min()}")
    st.write(f"**Peak Close:** {data1['Close'].max()}")
    st.write(f"**Peak Open:** {data1['Open'].max()}")

    st.write(f"**Company 2: {share2_name} ({share2})**")
    st.write(f"**Current Price:** {data2['Close'].iloc[-1]}")
    st.write(f"**Week High:** {data2['High'].max()}")
    st.write(f"**Week Low:** {data2['Low'].min()}")
    st.write(f"**Peak Close:** {data2['Close'].max()}")
    st.write(f"**Peak Open:** {data2['Open'].max()}")


    # Displaying real-time graph comparison
    st.subheader("Real-Time Share Price Comparison")


    # data for both shares
    st.line_chart({
        share1_name: data1['Close'],
        share2_name: data2['Close']
    })



if __name__ == "__main__":
    compare_page()