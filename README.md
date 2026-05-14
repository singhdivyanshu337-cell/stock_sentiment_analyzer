# 📈 AI Stock Market Sentiment Analyzer

AI-powered stock market sentiment analysis dashboard built using Python, Streamlit, NLP, and financial news data.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![AI](https://img.shields.io/badge/AI-NLP-black)
![Finance](https://img.shields.io/badge/Domain-Finance-green)
![Project](https://img.shields.io/badge/Project-Active-success)

---

# 📖 About The Project

The **AI Stock Market Sentiment Analyzer** is an internship-level financial analytics project that combines stock market data with Natural Language Processing (NLP) to analyze market sentiment from financial news headlines.

The application fetches real-time stock-related news, performs sentiment analysis using the VADER sentiment analyzer, and visualizes stock price movements through an interactive Streamlit dashboard.

This project demonstrates practical implementation of:
- Financial data analysis
- NLP sentiment analysis
- Data visualization
- API integration
- Streamlit dashboard development

---

# ✨ Features

- 📊 Real-time stock market dashboard
- 📰 Live financial news fetching using News API
- 🤖 Sentiment analysis using VADER NLP
- 📈 Candlestick stock chart visualization
- 📉 Positive / Neutral / Negative sentiment scoring
- 🔍 Company-wise stock analysis
- 🌐 Interactive Streamlit web interface
- ⚡ Fast and lightweight Python execution
- 📚 Beginner-friendly project structure
- 🧠 AI-powered market sentiment insights

---

# 🛠️ Tech Stack

## Programming Language
- Python 3.13

## Libraries Used
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Plotly
- yFinance
- NLTK
- VaderSentiment
- NewsAPI-Python

## APIs
- News API
- Yahoo Finance API (yFinance)

---

# 📂 Project Structure

```text
stock_sentiment_analyzer/
│
├── dashboard/
│   └── app.py
│
├── data/
│
├── scripts/
│   ├── __init__.py
│   ├── main.py
│   ├── news_fetcher.py
│   ├── sentiment_analyzer.py
│   ├── stock_data.py
│   └── visualization.py
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/singhdivyanshu337-cell/stock_sentiment_analyzer.git
```

---

## 2️⃣ Navigate Into Project Directory

```bash
cd stock_sentiment_analyzer
```

---

## 3️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib plotly yfinance nltk vaderSentiment newsapi-python streamlit
```

---

# ▶️ Run The Project

## Run Main Python File

```bash
python main.py
```

---

# 🌐 Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📊 Supported Companies

Currently tested with:
- Reliance
- TCS
- Infosys
- HDFC Bank

More companies can be analyzed dynamically through user input.

---

#  Dashboard Preview

## Features Included In Dashboard
- Market Watchlist
- Real-time stock prices
- Sentiment analysis panel
- Financial news headlines
- Candlestick stock charts
- Sentiment trend visualization

Screenshots will be added later.

---

# 🔄 Project Workflow Architecture

```text
User Input
     │
     ▼
Fetch Financial News ─────► News API
     │
     ▼
Sentiment Analysis ───────► VADER NLP
     │
     ▼
Fetch Stock Market Data ─► Yahoo Finance API
     │
     ▼
Generate Charts & Graphs
     │
     ▼
Display Interactive Dashboard
```

---

# 🧠 Sentiment Analysis Workflow

1. User enters company name
2. News headlines are fetched using News API
3. Headlines are analyzed using VADER sentiment analyzer
4. Sentiment scores are generated
5. Stock market data is fetched using yFinance
6. Candlestick charts and sentiment visuals are generated
7. Results are displayed on Streamlit dashboard

---

# 📈 Data Visualization

The project visualizes:
- Stock price trends
- Candlestick charts
- Market watchlists
- Sentiment score analysis
- News sentiment distribution

Visualization libraries used:
- Matplotlib
- Plotly
- Streamlit Charts

---

# 🔐 API Configuration

Create your News API key from:

https://newsapi.org/

Then add your API key inside:

```python
API_KEY = "YOUR_API_KEY"
```

---

# 🚀 Future Scope

- Add Machine Learning stock prediction
- Integrate Twitter/X sentiment analysis
- Add portfolio recommendation system
- Add moving average indicators
- Add technical indicators (RSI, MACD)
- Add real-time WebSocket updates
- Deploy project on AWS Cloud
- Add user authentication system
- Improve dashboard UI/UX
- Add multi-company comparison support
- Integrate advanced transformer NLP models

---

# ☁️ Deployment Options

This project can be deployed using:
- Streamlit Cloud
- AWS EC2
- Render
- Railway
- Docker

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- API Integration
- NLP Sentiment Analysis
- Financial Data Handling
- Data Visualization
- Streamlit Dashboard Development
- Python Project Structuring
- Real-time Market Analytics
- GitHub Project Management

---

# 🤝 Contribution

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

# 📌 Repository Topics

```text
python
nlp
ai
machine-learning
finance
stock-market
streamlit
dashboard
financial-analysis
sentiment-analysis
```

---

# 👨‍💻 Author

Divyanshu Singh

## GitHub
https://github.com/singhdivyanshu337-cell

---

# 🏆 Project Highlights

✅ AI-Based Sentiment Analysis  
✅ Real-time Financial News Processing  
✅ Interactive Streamlit Dashboard  
✅ Candlestick Stock Charts  
✅ NLP Integration  
✅ Beginner-Friendly Architecture  
✅ Internship-Level Portfolio Project  

---

# 🙌 Acknowledgements

Special thanks to:
- Streamlit
- News API
- Yahoo Finance
- NLTK
- Open-source Python community

---

# 💡 Why This Project Matters

Stock market sentiment plays a major role in understanding investor psychology and market behavior. This project demonstrates how Artificial Intelligence and NLP can be used to extract valuable insights from financial news data and combine them with real-time stock analysis.

---
