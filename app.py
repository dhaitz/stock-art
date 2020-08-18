# coding: utf-8

import streamlit as st
import datetime
import matplotlib.pyplot as plt

import functions


# img vars
img = plt.imread("img/pexels-mamunurpics-3930012.jpg")
x_width_image = 4892
horizon_height = 1480

################################################################################
# App layout
################################################################################

# Sidebar
st.sidebar.markdown("Look up ticker symbols [here](https://finance.yahoo.com/lookup)")
ticker_symbol = st.sidebar.text_input('Stock ticker symbol', value='AAPL')
start_date = st.sidebar.date_input("Start day", datetime.date(2010, 8, 14))
end_date = st.sidebar.date_input("End day", datetime.date(2020, 8, 14))

# Main Window

st.title("Stock Price Chart")

# Function calls to get data and make image
df_ticker = functions.get_stock_data(ticker_symbol, start_date, end_date)
stock_prices = functions.prepare_data(df_ticker['Close'])
fig = functions.make_picture(stock_prices, img=img, x_width_image=x_width_image, horizon_height=horizon_height)
st.pyplot(fig=fig, bbox_inches='tight')
plt.close(fig)

st.markdown("Suggestions [welcome](https://github.com/dhaitz/stock-art). Image source: [mamunurpics](https://www.pexels.com/@mamunurpics). Inspired by [stoxart](https://www.stoxart.com).")

# workaround to open in wide mode (https://github.com/streamlit/streamlit/issues/314#issuecomment-579274365)
max_width_str = f"max-width: 1000px;"
st.markdown(f"""<style>.reportview-container .main .block-container{{ {max_width_str} }}</style>""", unsafe_allow_html=True)
