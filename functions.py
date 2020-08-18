
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

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


def make_picture(stock_prices, img, x_width_image, horizon_height):
    """x_width_image: dedicated arg for more control, instead of taking image dim"""

    fig, ax = plt.subplots()
    ax.imshow(img)

    x = np.linspace(0, x_width_image, len(stock_prices))

    ax.fill_between(x, stock_prices, horizon_height, color='#081A1C')

    plt.axis('off')
    plt.tight_layout()
    return fig
