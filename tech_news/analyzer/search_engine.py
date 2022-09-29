# Requisito 6
from tech_news.database import search_news
from datetime import datetime


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
    try:
        date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    db_query = {"timestamp": {"$regex": date, "$options": "i"}}
    titles_and_urls = []
    news_by_title = search_news(db_query)
    for new in news_by_title:
        titles_and_urls.append((new["title"], new["url"]))
    return titles_and_urls


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
