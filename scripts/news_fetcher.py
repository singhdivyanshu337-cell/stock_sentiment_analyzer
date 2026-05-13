from newsapi import NewsApiClient

API_KEY = "20de4ef2e4cb4495b22eab3d616796b9"

newsapi = NewsApiClient(api_key=API_KEY)


def get_news(company):

    queries = [
        f'{company} stock OR {company} shares',
        f'{company} earnings OR {company} results',
        f'{company}'
    ]

    headlines = []

    for query in queries:

        articles = newsapi.get_everything(
            q=query,
            language="en",
            sort_by="publishedAt",
            page_size=10,
            domains="economictimes.indiatimes.com,moneycontrol.com,bloomberg.com,reuters.com"
        )

        for article in articles["articles"]:
            title = article["title"]

            if company.lower() in title.lower():
                headlines.append(title)

        # If we got enough news, stop early
        if len(headlines) >= 10:
            break

    return headlines 