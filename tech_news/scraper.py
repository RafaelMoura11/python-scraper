import requests
import time
from parsel import Selector


header = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(headers=header, url=url)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = selector.css("h2 a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_button = selector.css(".next.page-numbers::attr(href)").get()
    return next_page_button


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("""head link[rel="canonical"]::attr(href)""").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    author = selector.css("li.meta-author span.author a::text").get()
    category = selector.css("span.label::text").get()
    comments_count = selector.css("article.comment-body").getall()
    summary = "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip()
    tags = selector.css(".post-tags a::text").getall(),

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author,
        "comments_count": len(comments_count),
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
