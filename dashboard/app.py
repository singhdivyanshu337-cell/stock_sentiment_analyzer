import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

from scripts.news_fetcher import get_news
from scripts.sentiment_analyzer import analyze_sentiment
from scripts.stock_data import get_stock_data
from scripts.visualization import plot_sentiment


# ---------------- UI CONFIG ----------------
st.set_page_config(
    page_title="Stock Sentiment Analyzer",
    layout="wide",
    page_icon="📈"
)

st.title("📊 AI Stock Market Sentiment Analyzer")

st.markdown("---")


# ---------------- WATCHLIST (REAL TIME) ----------------
st.subheader("📌 Market Watchlist")

watchlist = {
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "Tata Motors": "TATAMOTORS.NS"
}

cols = st.columns(len(watchlist))

for i, (name, ticker) in enumerate(watchlist.items()):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")

    if not data.empty:
        price = round(data["Close"].iloc[-1], 2)
        change = round(data["Close"].iloc[-1] - data["Open"].iloc[-1], 2)

        cols[i].metric(
            label=name,
            value=f"₹ {price}",
            delta=f"{change}"
        )

st.markdown("---")


# ---------------- INPUT ----------------
company = st.text_input(
    "Enter Company Name (Reliance, TCS, Infosys, etc.)"
)


# ---------------- AUTO TICKER ----------------
def get_auto_ticker(company):
    company = company.lower()

    mapping = {
        "reliance": "RELIANCE.NS",
        "tcs": "TCS.NS",
        "tata": "TATAMOTORS.NS",
        "infosys": "INFY.NS",
        "hdfc": "HDFCBANK.NS",
        "icici": "ICICIBANK.NS",
        "wipro": "WIPRO.NS",
        "sbi": "SBIN.NS",
        "adani": "ADANIENT.NS"
    }

    for key in mapping:
        if key in company:
            return mapping[key]

    return None


# ---------------- BUTTON ----------------
if st.button("🔍 Analyze Stock"):

    if company == "":
        st.warning("Please enter a company name")
        st.stop()

    ticker = get_auto_ticker(company)

    # create columns FIRST (fix for col1 error)
    col1, col2 = st.columns([1, 1])

    # ================= LEFT SIDE — NEWS SENTIMENT =================
    with col1:
        st.subheader("📰 News Sentiment")

        results = []

        with st.spinner("Fetching news..."):
            news_list = get_news(company)

        if not news_list:
            st.error("No relevant news found")
        else:
            total_score = 0

            for news in news_list:
                sentiment = analyze_sentiment(news)

                results.append({
                    "news": news,
                    "score": sentiment["score"],
                    "sentiment": sentiment["sentiment"]
                })

                total_score += sentiment["score"]

            avg_score = total_score / len(results)

            st.metric("Average Sentiment Score", round(avg_score, 3))

            if avg_score > 0.2:
                st.success("Bullish 📈")
            elif avg_score < -0.2:
                st.error("Bearish 📉")
            else:
                st.info("Neutral 😐")

            scores = [r["score"] for r in results]
            fig_sent = plot_sentiment(scores)
            st.pyplot(fig_sent)

    # ================= RIGHT SIDE — STOCK PRICE =================
    with col2:
        st.subheader("📉 Stock Price")

        if ticker is None:
            st.warning("Ticker not found")
        else:
            df = get_stock_data(ticker)

            if df is None or df.empty:
                st.warning("No stock data")
            else:
                fig = go.Figure(
                    data=[
                        go.Candlestick(
                            x=df.index,
                            open=df["Open"],
                            high=df["High"],
                            low=df["Low"],
                            close=df["Close"]
                        )
                    ]
                )

                fig.update_layout(
                    title=f"{company.upper()} Candlestick Chart",
                    xaxis_title="Date",
                    yaxis_title="Price",
                    height=500
                )

                st.plotly_chart(fig, use_container_width=True)

    # ================= NEWS LIST =================
    st.markdown("---")
    st.subheader("🗞 Latest News")

    if results:
        for item in results[:5]:
            st.write(f"**{item['news']}**")
            st.write(f"Sentiment: {item['sentiment']}")
            st.write(f"Score: {item['score']}")
            st.write("---")
    else:
        st.info("No news to display")