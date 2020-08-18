# coding: utf-8

import streamlit as st
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import numpy as np


# Title
st.title("Stock Price Chart")
st.sidebar.markdown("Look up ticker symbols [here](https://finance.yahoo.com/lookup)")
ticker_symbol = st.sidebar.text_input('Stock ticker symbol', value='AAPL')
start_date = st.sidebar.date_input("Start day", datetime.date(2010, 8, 14))
end_date = st.sidebar.date_input("End day", datetime.date(2020, 8, 14))


def get_stock_data(tickerSymbol, start_date, end_date):

    tickerData = yf.Ticker(tickerSymbol)
    df_ticker = tickerData.history(period='1d', start=start_date, end=end_date)
    return df_ticker


def prepare_data(s):
    ymax = 1000
    s = s * ymax / s.max()  # scale y range
    s = 1450 -s # image top left is (0,0), so horizon line is around -1450, plot should be above that

    # smoothen
    window_size = len(s) // 150
    s = s.rolling(window_size, min_periods=1).mean()

    return s


def make_picture(stock_prices, img):
    fig, ax = plt.subplots()
    ax.imshow(img)

    x_width_image = 4892
    x = np.linspace(0, x_width_image, len(stock_prices))

    horizon_height = 1480
    ax.fill_between(x, stock_prices, horizon_height, color='#081A1C')

    plt.axis('off')
    plt.tight_layout()
    return fig

img = plt.imread("img/pexels-mamunurpics-3930012.jpg")
df_ticker = get_stock_data(ticker_symbol, start_date, end_date)
stock_prices = prepare_data(df_ticker['Close'])

fig = make_picture(stock_prices, img)

# Draw plot
st.pyplot(fig=fig, bbox_inches='tight')
plt.close(fig)

st.markdown("Suggestions [welcome](https://github.com/dhaitz/stock-art). Image source: [mamunurpics](https://www.pexels.com/@mamunurpics). Inspired by [stoxart](https://www.stoxart.com).")

# workaround to open in wide mode (https://github.com/streamlit/streamlit/issues/314#issuecomment-579274365)
max_width_str = f"max-width: 1000px;"
st.markdown(f"""<style>.reportview-container .main .block-container{{ {max_width_str} }}</style>""", unsafe_allow_html=True)
