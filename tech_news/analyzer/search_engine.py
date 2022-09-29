# Requisito 6
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    db_query = {"title": {"$regex": title, "$options": "i"}}
    news_by_title = search_news(db_query)
    titles_and_urls = []
    for new in news_by_title:
        titles_and_urls.append((new["title"], new["url"]))
    return titles_and_urls


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
