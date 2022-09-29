from tech_news.database import search_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = search_news({})
    sorted_news = sorted(
        all_news, key=itemgetter('comments_count'), reverse=True)
    titles_and_urls = []
    for new in sorted_news:
        titles_and_urls.append((new["title"], new["url"]))
        if 5 < len(titles_and_urls):
            return titles_and_urls[0:5]
        return titles_and_urls


# Requisito 11
def top_5_categories():
    all_news = search_news({})
    sorted_news = sorted(
        all_news, key=itemgetter('category'), reverse=True)
    categories = []
    for new in sorted_news:
        categories.append(new["category"])
        if 5 < len(categories):
            return categories[0:5]
        else:
            return categories
