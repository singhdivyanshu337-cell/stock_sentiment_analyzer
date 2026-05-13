from news_fetcher import get_news
from scripts.sentiment_analyzer import analyze_sentiment


def main():
    company = input("Enter company name (e.g. Reliance, Tata): ")

    print("\nFetching news...\n")

    news_list = get_news(company)

    # Check if news exists
    if not news_list:
        print("No relevant news found.")
        return

    results = []

    for news in news_list:
        sentiment_result = analyze_sentiment(news)

        results.append({
            "news": news,
            "sentiment": sentiment_result["sentiment"],
            "score": sentiment_result["score"]
        })

    print("\n--- Sentiment Analysis Result ---\n")

    total_score = 0

    for item in results:
        print(f"News: {item['news']}")
        print(f"Sentiment: {item['sentiment']}")
        print(f"Score: {item['score']}")
        print("-" * 50)

        total_score += item["score"]

    # 🔥 Average sentiment (VERY IMPORTANT)
    avg_score = total_score / len(results)

    print("\n=== Overall Sentiment ===")
    print(f"Average Score: {avg_score}")

    if avg_score > 0.2:
        print("Overall Sentiment: Bullish 📈")
    elif avg_score < -0.2:
        print("Overall Sentiment: Bearish 📉")
    else:
        print("Overall Sentiment: Neutral 😐")


if __name__ == "__main__":
    main()