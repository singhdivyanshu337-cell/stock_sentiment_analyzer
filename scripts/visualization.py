import matplotlib.pyplot as plt

def plot_stock_price(df, company):
    plt.figure()

    plt.plot(df.index, df["Close"])
    plt.title(f"{company} Stock Price (Last 7 Days)")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt


def plot_sentiment(scores):
    plt.figure()

    plt.plot(scores)
    plt.title("Sentiment Trend")
    plt.xlabel("News Index")
    plt.ylabel("Sentiment Score")

    return plt