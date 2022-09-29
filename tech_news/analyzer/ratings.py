from tech_news.database import search_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = search_news({})
    sorted_news = sorted(
        all_news, key=itemgetter('comments_count'), reverse=True)
    if len(sorted_news) > 5:
        return sorted_news[0:5]
    return sorted_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
