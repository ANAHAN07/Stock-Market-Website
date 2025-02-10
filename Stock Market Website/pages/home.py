import streamlit as st
import yfinance as yf
import pandas as pd



# Function to fetch stock data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist


# Function to fetch latest financial news
def get_latest_news():
    return [
        {"title": "Stock Market Hits Record Highs", "url": "https://www.investopedia.com/dow-jones-today-01232025-8778974"},        # Stock Market Hits Record Highs New
        {"title": "Tech Stocks See Massive Growth", "url": "https://finance.yahoo.com/news/tech-stocks-face-enormous-task-171800542.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGPGatYkkppRnt-hMFd0dbx0G3BcEUimh1TjRxln_9tCLAIY1Wd0ackL4YpJu-TCnYrU5Duhw6dMSqfjN6-zuGJVBTXTXHeROVICOYsfHd5dsJFd8LghXB-o-JZr5DHEL3XdHPNfq-QUzd5vKycx8ignNbtjlkBYJLcTQjb3fT8p"},       # Tech Stocks See Massive Growth News
        {"title": "Forex Market Sees Volatility Amid Economic Shifts", "url": "https://www.thedailystar.net/business/economy/news/bb-plans-raise-exchange-rate-amid-forex-volatility-3788281"}      # Forex Market Sees Volatility Amid Economic Shifts News
    ]


# List of stock exchanges and commodities
stock_exchanges = [
    {"Stock Market Name": "New York Stock Exchange", "Code": "NYSE", "Country": "USA"},
    {"Stock Market Name": "Nasdaq Stock Market", "Code": "NASDAQ", "Country": "USA"},
    {"Stock Market Name": "London Stock Exchange", "Code": "LSE", "Country": "UK"},
    {"Stock Market Name": "Tokyo Stock Exchange", "Code": "TSE", "Country": "Japan"},
    {"Stock Market Name": "Shanghai Stock Exchange", "Code": "SSE", "Country": "China"},
    {"Stock Market Name": "Hong Kong Stock Exchange", "Code": "HKEX", "Country": "Hong Kong"},
    {"Stock Market Name": "Euronext", "Code": "ENX", "Country": "Europe"},
    {"Stock Market Name": "Toronto Stock Exchange", "Code": "TSX", "Country": "Canada"},
    {"Stock Market Name": "Australian Securities Exchange", "Code": "ASX", "Country": "Australia"},
    {"Stock Market Name": "Bombay Stock Exchange", "Code": "BSE", "Country": "India"},
    {"Stock Market Name": "National Stock Exchange of India", "Code": "NSE", "Country": "India"},
    {"Stock Market Name": "Deutsche Börse (Frankfurt Stock Exchange)", "Code": "FWB", "Country": "Germany"},
    {"Stock Market Name": "SIX Swiss Exchange", "Code": "SIX", "Country": "Switzerland"},
    {"Stock Market Name": "Korea Exchange", "Code": "KRX", "Country": "South Korea"},
    {"Stock Market Name": "Taiwan Stock Exchange", "Code": "TWSE", "Country": "Taiwan"},
    {"Stock Market Name": "Singapore Exchange", "Code": "SGX", "Country": "Singapore"},
    {"Stock Market Name": "Johannesburg Stock Exchange", "Code": "JSE", "Country": "South Africa"},
    {"Stock Market Name": "São Paulo Stock Exchange", "Code": "B3", "Country": "Brazil"},
    {"Stock Market Name": "Moscow Exchange", "Code": "MOEX", "Country": "Russia"},
    {"Stock Market Name": "Dhaka Stock Exchange", "Code": "DSE", "Country": "Bangladesh"},
]


# Oil Stock Names and Codes
oil_stock =[    
    {"Stock Market Name": "Brent Crude Oil", "Code": "BZ=F", "Country": "Global"},
    {"Stock Market Name": "West Texas Intermediate Oil", "Code": "CL=F", "Country": "USA"},
]


# Coin Stock Names and Codes
coin_list = [
    {"Coin": "Bitcoin", "Ticker": "BTC-USD"},
    {"Coin": "Ethereum", "Ticker": "ETH-USD"},
    {"Coin": "Binance Coin", "Ticker": "BNB-USD"},
    {"Coin": "Ripple", "Ticker": "XRP-USD"},
    {"Coin": "Cardano", "Ticker": "ADA-USD"}
]


# Ore Stock Names and Codes
ore =[
        {"Ore": "Gold", "Code": "XAU-USD", "Details": "Spot Price"},
        {"Ore": "Gold", "Code": "GLD", "Details": "SPDR Gold Trust ETF"},
        {"Ore": "Gold", "Code": "NEM", "Details": "Newmont Corporation (Gold mining)"},
        {"Ore": "Iron", "Code": "BHP", "Details": "BHP Group (Iron Ore)"},
        {"Ore": "Iron", "Code": "RIO", "Details": "Rio Tinto (Iron Ore)"},
        {"Ore": "Iron", "Code": "VALE", "Details": "Vale S.A. (Iron Ore)"},
        {"Ore": "Platinum", "Code": "XPT-USD", "Details": "Platinum Spot Price"},
        {"Ore": "Platinum", "Code": "PPLT", "Details": "ETF for Platinum"},
        {"Ore": "Platinum", "Code": "SBSW", "Details": "Sibanye Stillwater (Platinum mining)"}
]


# Converting to DataFrame
df = pd.DataFrame(stock_exchanges)
dx = pd.DataFrame(oil_stock)
dc = pd.DataFrame(coin_list)
de = pd.DataFrame(ore)



# Home Page Function
def home_page():
    st.title("Stock Market Dashboard")      # Stock Market Dashboard

    # Latest Stock and Forex News
    st.subheader("Latest Stock and Forex News")
    news_items = get_latest_news()
    for news in news_items:
        st.markdown(f"[🔹 {news['title']}]({news['url']})")

    # Live Hot Share Graph
    st.subheader("Live Hot Share Graph")
    stock_ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT)", "NVDA")
    if stock_ticker:
        data = get_stock_data(stock_ticker)
        if not data.empty:
            st.line_chart(data['Close'])
        else:
            st.write("No data available for this ticker.")


    # QNA


    # Trading Information
    st.subheader("What is Trading?")
    st.write("""
Trading is the process of buying and selling financial assets like 
stocks, bonds, commodities, and currencies with the goal of making a profit. 
It can be done on various platforms, such as stock exchanges, forex markets, and cryptocurrency exchanges.""")


    # Stock Market Information
    st.subheader("What is the Share Market?")
    st.write("""
The share market (or stock market) is a marketplace 
where investors buy and sell shares of publicly listed companies. It is divided into:""")
    st.write("📊 - **Primary Market** - Where companies issue new shares to the public (Initial Public Offering or IPO).")
    st.write("📊 - **Secondary Market** - Where existing shares are traded among investors.")
    st.write("📊 Major stock exchanges include:")
    st.write("📊 - New York Stock Exchange (NYSE)")
    st.write("📊 - Nasdaq")
    st.write("📊 - London Stock Exchange (LSE)")
    st.write("📊 - Tokyo Stock Exchange (TSE)")
    st.write("📊 - Dhaka Stock Exchange (DSE)")


    # Forex Market Information
    st.subheader("What is the Forex Market?")
    st.write("The Forex (Foreign Exchange) Market is the world's largest financial market, where currencies are traded.")
    st.write("Forex trading pairs include:")
    st.write("💹 - **Major Pairs** - EUR/USD, GBP/USD, USD/JPY")
    st.write("💹 - **Minor Pairs** - EUR/GBP, GBP/JPY")
    st.write("💹- **Exotic Pairs** - USD/BDT, EUR/TRY")
    st.write("Forex trading is influenced by economic indicators, geopolitical events, and central bank policies.")


    # Stock Information
    st.subheader("What are Stocks?")
    st.write("Stocks represent ownership in a company. When you buy a stock, you own a small part of that company. Companies issue stocks to raise capital for expansion.")
    st.write("Stocks can be categorized into:")
    st.write("📈 - **Common Stocks** - Provide voting rights and dividends.")
    st.write("📈 - **Preferred Stocks** - Provide fixed dividends but no voting rights.")
    st.write("Stocks are traded in the stock market and their prices fluctuate based on supply, demand, and company performance.")
    

    # List of Stocks
    st.subheader("How Many Stocks Are There?")
    st.write("There are thousands of publicly traded stocks globally. Some major ones include:")
    st.write("🛒 - Apple Inc. (AAPL)")
    st.write("🛒 - Microsoft Corp. (MSFT)")
    st.write("🛒 - Tesla Inc. (TSLA)")
    st.write("🛒 - Amazon Inc. (AMZN)")
    st.write("🛒 - Google (Alphabet Inc.) (GOOGL)")
    st.write("🛒 - Nvidia Corp. (NVDA)")
    st.write("🛒 - Meta (Facebook) (META)")
    st.write("🛒 - Berkshire Hathaway (BRK.A)")
    st.write("🛒 - JP Morgan Chase (JPM)")
    st.write("🛒 - Johnson & Johnson (JNJ)")


    # Candlestick Patterns
    st.subheader("What are Candlestick Patterns?")
    st.write("Candlestick patterns are a type of price chart used in technical analysis to predict future price movements. Each candlestick represents four key prices:")
    st.write("🔓 - **Open** - The price at which trading started.")
    st.write("🔒 - **Close** - The price at which trading ended.")
    st.write("⬆️ - **High** - The highest price reached.")
    st.write("⬇️ - **Low** - The lowest price reached.")

    st.write("✅ **Types of Candlestick Patterns:**")
    st.write("**Bullish Patterns (Indicate price increase)**")
    st.write("🔨 - Hammer")
    st.write("- Bullish Engulfing")
    st.write("⭐ - Morning Star")

    st.write("✅ **Bearish Patterns (Indicate price decrease)**")
    st.write("💥 - Shooting Star")
    st.write("- Bearish Engulfing")
    st.write("🌟 - Evening Star")

    st.write("These patterns help traders make informed decisions about buying or selling stocks.")


    # Display stock exchanges and commodities
    st.subheader("📊 List of Major Stock Exchanges")
    st.dataframe(df)  # Display stock exchanges and commodities in a table format

    st.subheader("Oil Share List")
    st.dataframe(dx)

    st.subheader("Coin Share List")
    st.dataframe(dc)

    st.subheader("Ore Share List")
    st.dataframe(de)


    # General Islamic Perspective on Trading
    st.subheader("**General Islamic Perspective on Trading**")
    st.write("""
In Islam, trade and business are generally halal as long as they follow Shariah
(Islamic law) principles. However, certain types of trading can become haram if they involve elements like:""")
    st.write("""
✅ Halal Trading Practices\n
✔️ Buying and selling assets (stocks, commodities, currencies, etc.) with proper ownership.\n
✔️ Avoiding companies involved in haram industries (e.g., alcohol, gambling, pork, riba-based banks).\n
✔️ Trading with full transparency (no fraud, deception, or insider trading).\n
✔️ Risk-sharing rather than engaging in speculation.\n
\n
❌ Haram Trading Practices\n
⛔ Riba (Interest-based Trading) - Buying and selling with interest (like margin trading with interest).\n
⛔ Gharar (Uncertainty) - Trading that involves excessive uncertainty (like options or high-risk speculation).\n
⛔ Short Selling - Selling something you do not own.\n
⛔ High-Leverage Trading - Forex and CFD trading often involve excessive leverage, which is considered gambling-like behavior.\n
⛔ Day Trading & Speculation - If done like gambling (without research or proper ownership), it can be haram.
""")


    # Stock Market Trading: Halal or Haram?
    st.subheader("Stock Market Trading: Halal or Haram?")
    st.write("""
✔ Investing in halal stocks (companies with ethical and Shariah-compliant businesses) is permissible.\n
✔ Long-term investing is recommended over speculation.\n
❌ Day trading with speculation may be haram if it involves gambling-like behavior.\n
""")


    # Forex Trading: Halal or Haram?
    st.subheader("Forex Trading: Halal or Haram?")
    st.write("""
Forex trading can be haram if it involves interest (riba), excessive speculation, 
or leverage. Some Islamic forex accounts remove interest, but scholars still debate whether they are truly Shariah-compliant.
""")


    # Cryptocurrency: Halal or Haram?
    st.subheader("Cryptocurrency: Halal or Haram?")
    st.write("""
Scholars have different opinions. If used as a legitimate asset with 
clear ownership and purpose, it may be halal. But highly speculative crypto trading 
(like meme coins, pump & dump schemes) is more like gambling and is haram.
""")


    # Conclusion
    st.subheader("Conclusion")
    st.write("""
✔ Halal trading follows Islamic finance principles - ethical, transparent, and free from riba, gharar, and speculation.\n
❌ Haram trading involves uncertainty, gambling, interest, and unethical business practices.
""")
    

    # Difference Between Trading and Gambling
    st.subheader("Difference Between Trading and Gambling")
    st.write("""
Many people compare trading (stocks, forex, crypto, etc.) to gambling, but they are fundamentally different. 
The key difference lies in risk management, strategy, and ownership.
""")
    st.write("""
Ownership:\n
Trading 📈:\n
Involves buying assets (stocks, commodities, currencies) that have real value.\n
Gambling 🎰:\n
No ownership—bets are placed on random outcomes.
""")
    st.write("""
Risk Control:\n
Trading 📈:\n
Traders use strategies, research, and analysis to manage risk.\n
Gambling 🎰:\n
Gambling relies on chance with no real control over risk.
""")
    st.write("""
Decision Basis:\n
Trading 📈:\n
Decisions are made using technical & fundamental analysis.\n
Gambling 🎰:\n
Decisions are made based on luck or probability.
""")
    st.write("""
Legal & Ethical:\n
Trading 📈:\n
Recognized as a legitimate financial activity.\n
Gambling 🎰:\n
Often restricted or illegal in many places.
""")
    st.write("""
Return Expectation:\n
Trading 📈:\n
Long-term gains are possible through skill and strategy.\n
Gambling 🎰:\n
The house (casino) always has an edge—losses are likely in the long run.
""")
    st.write("""
Skill vs. Luck:\n
Trading 📈:\n
Requires skills, knowledge, experience, and risk management.\n
Gambling 🎰:\n
Mostly dependent on luck or probability.
""")


    # Key Differences Explained
    st.subheader("Key Differences Explained")
    st.write("""
✅ Trading is an investment activity where you analyze markets, assess risks, and own assets.\n
❌ Gambling is a game of chance where the outcome is unpredictable and based on luck.\n

👉 Example:\n

Buying shares of Apple (AAPL) after analyzing their financials = Trading ✅\n
Betting on a roulette wheel or a football match without control = Gambling ❌
""")
    


if __name__ == "__main__":
    home_page()