import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# Function to calculate profit/loss
def calculate_profit_loss(buy_price, sell_price, shares):
    total_cost = buy_price * shares
    total_revenue = sell_price * shares
    profit_loss = total_revenue - total_cost
    percent_change = ((sell_price - buy_price) / buy_price) * 100
    return profit_loss, percent_change



def calculator_page():
    st.title("📈 Stock Profit & Loss Calculator")

    # User input area
    buy_price = st.number_input("Enter Buy Price (per share)", min_value=0.01, format="%.2f")
    sell_price = st.number_input("Enter Sell Price (per share)", min_value=0.01, format="%.2f")
    shares = st.number_input("Enter Number of Shares", min_value=1, step=1)

    # Calculating result
    if st.button("Calculate"):
        if buy_price > 0 and sell_price > 0 and shares > 0:
            profit_loss, percent_change = calculate_profit_loss(buy_price, sell_price, shares)

            # Displaying results
            if profit_loss > 0:
                st.success(f"🎉 Profit: ${profit_loss:.2f} (+{percent_change:.2f}%)")
            elif profit_loss < 0:
                st.error(f"📉 Loss: ${abs(profit_loss):.2f} ({percent_change:.2f}%)")
            else:
                st.info("⚖️ No Profit, No Loss (Break-even)")


            fig, ax = plt.subplots()
            ax.bar(["Profit/Loss"], [profit_loss], color="green" if profit_loss > 0 else "red")
            ax.set_ylabel("Amount ($)")
            ax.set_title("Profit/Loss Overview")
            st.pyplot(fig)
        else:
            st.warning("Please enter valid values.")



if __name__ == "__main__":
    calculator_page()