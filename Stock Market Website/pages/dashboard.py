import streamlit as st
import yfinance as yf


def get_stock_data(ticker):         # historical stock data for the given ticker
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist


def dashboard_page():
    st.title("📊 Stock Market Dashboard")
    
    # Stock selection
    stock_ticker = st.selectbox("Select a Stock", [
        "AAPL", "MSFT", "TSLA", "AMZN", "GOOGL", "NVDA", "META", "BRK.A", "JPM", "JNJ"              # More in future
    ])                                              
    

    # display stock data
    if stock_ticker:
        data = get_stock_data(stock_ticker)
        
        if not data.empty:
            st.subheader(f"Stock Price History: {stock_ticker}")
            st.line_chart(data['Close'])
            
            st.subheader("Stock Details")                       # Showing Stock Details
            stock_info = yf.Ticker(stock_ticker).info
            st.write(f"**Company Name:** {stock_info.get('longName', 'N/A')}")
            st.write(f"**Current Price:** ${stock_info.get('currentPrice', 'N/A')}")
            st.write(f"**Market Cap:** {stock_info.get('marketCap', 'N/A')}")
            st.write(f"**52-Week High:** ${stock_info.get('fiftyTwoWeekHigh', 'N/A')}")
            st.write(f"**52-Week Low:** ${stock_info.get('fiftyTwoWeekLow', 'N/A')}")
        else:
            st.error("No data available for this stock ticker.")



if __name__ == "__main__":
    dashboard_page()