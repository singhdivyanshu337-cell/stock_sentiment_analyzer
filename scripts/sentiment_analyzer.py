from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    text_lower = text.lower()

    positive_keywords = ["surge", "rally", "gain", "rise", "jump", "soar", "profit", "growth"]
    negative_keywords = ["fall", "drop", "decline", "loss", "crash", "down", "slump"]

    # Get VADER score
    score = analyzer.polarity_scores(text)
    compound = score['compound']

    # Adjust score based on finance keywords
    if any(word in text_lower for word in positive_keywords):
        compound += 0.2
    elif any(word in text_lower for word in negative_keywords):
        compound -= 0.2

    # Final sentiment decision
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "score": round(compound, 3)
    }