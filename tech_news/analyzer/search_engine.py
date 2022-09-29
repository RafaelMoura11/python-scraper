# Requisito 6
from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
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
    titles_and_urls = []
    news_by_date = search_news({"timestamp": {"$regex": date}})
    for new in news_by_date:
        titles_and_urls.append((new["title"], new["url"]))
    return titles_and_urls


# Requisito 8
def search_by_tag(tag):
    titles_and_urls = []
    news_by_tag = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}})
    for new in news_by_tag:
        titles_and_urls.append((new["title"], new["url"]))
    return titles_and_urls


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news_by_category = search_news(
        {"category": {"$regex": category, "$options": "i"}})
    titles_and_urls = []
    for new in news_by_category:
        titles_and_urls.append((new["title"], new["url"]))
    return titles_and_urls
