import streamlit as st
import pandas as pd

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


def learn_trading():
    st.title("Learn Trading 📚")

    st.header("Articles & Resources")
    st.write("Here you can find some articles and resources to improve your trading knowledge.")

    # articels 
    st.subheader("📘 Understanding Stock Market Basics")
    st.markdown("""
        - The stock market allows buyers and sellers to exchange ownership of publicly traded companies.
        - In trading, investors aim to buy low and sell high to make a profit.
        - [Link to an article on Stock Market Basics](https://www.investopedia.com/articles/investing/082614/how-stock-market-works.asp#:~:text=Stock%20markets%20are%20organized%20platforms,value%20and%20overall%20market%20conditions.)
    """)

    st.subheader("📚 Trading Strategies for Beginners")
    st.markdown("""
        - There are many strategies, including day trading, swing trading, and long-term investing.
        - [Link to an article on Trading Strategies](https://www.investopedia.com/trading-strategies-4689646)
    """)

    st.subheader("📈 Technical Analysis Basics")
    st.markdown("""
        - Technical analysis involves studying past market data to forecast future price movements.
        - [Link to an article on Technical Analysis](https://www.investopedia.com/terms/t/technicalanalysis.asp)
    """)

    st.subheader("📉 Risk Management in Trading")
    st.markdown("""
        - Risk management is crucial for protecting capital while trading.
        - [Link to an article on Risk Management](https://online.hbs.edu/blog/post/risk-management)
    """)

    # Pdf files
    st.header("Learning from PDFs 📑")
    st.write("Download these PDFs for deeper insights on trading.")


    st.subheader("📄 Trading Basics PDF")
    st.markdown("[Trading Basics](https://cdn.prod.website-files.com/652ef50b133e70ca4c917843/66a587b18253ff817639b40d_Basics%20of%20Trading%20%20.pdf)")

    st.subheader("📄 Complete Guide PDF")
    st.markdown("[Complete Guide](https://cdn.website-editor.net/25dd89c80efb48d88c2c233155dfc479/files/uploaded/The-Complete-Guide-to-Trading.pdf)")

    st.subheader("📄 Technical Analysis PDF")
    st.markdown("[Technical Analysis])(https://royalcapitalbd.com/download/research/Technical-Analysis-Tutorial.pdf)")

    st.subheader("📄 Risk Management PDF")
    st.markdown("[Risk Management](https://extensionrme.org/Pubs/Introduction-to-Risk-Management-ENGLISH.pdf)")

    st.subheader("📄 SEC Trading Basics PDF")
    st.markdown("[SEC Trading Basics](https://www.sec.gov/files/trading101basics.pdf)")

    st.subheader("📄 Risk Management and Tools PDF")
    st.markdown("[Risk Management and Tools](https://www.wcoomd.org/-/media/wco/public/global/pdf/topics/enforcement-and-compliance/activities-and-programmes/risk-management-and-intelligence/volume-1_annex.pdf)")

    st.subheader("📄 Trading for begginers PDF")
    st.markdown("[Trading for begginers](https://www.scribd.com/doc/147304406/Trading-for-Beginners)")

    st.subheader("📄 Basics Of Stock Market PDF")
    st.markdown("[Basics Of Stock Market](https://www.flame.edu.in/pdfs/fil/presentations/FIL_Stock%20Market.pdf)")

    st.subheader("📄 Forex Trading for begginers PDF")
    st.markdown("[Forex Trading for begginers](https://www.vantagemarkets.com/pdf/Forex-Trading-For-Beginners-The-Ultimate-Guide.pdf)")

    st.subheader("📄 58 Candlestick Patterns PDF")
    st.markdown("[58 Candlestick Patterns](https://www.scribd.com/document/697170728/58-Candlestick-Patterns-Trading-PDF-1)")

    st.subheader("📄 candlestick charts PDF")
    st.markdown("[candlestick charts](https://www.nseandbse.com/wp-content/uploads/2017/08/candlestickbook.pdf)")

    # st.subheader("📄  PDF")
    # st.markdown("[]()")


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
    learn_trading()