import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)

    # Get last 7 days data
    df = stock.history(period="7d")

    return df