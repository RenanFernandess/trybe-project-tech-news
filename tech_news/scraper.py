import time
import requests
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    HEADERS = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        response = requests.get(url, headers=HEADERS, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    container = selector.css(
        "div.archive-main a.cs-overlay-link::attr(href)"
    ).getall()
    return container


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    try:
        selector = parsel.Selector(text=html_content)
        return selector.css("nav.navigation a.next").attrib["href"]
    except KeyError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    return dict(
        url=selector.css("head > link[rel='canonical']::attr(href)").get(),
        title=selector.css("div.entry-header-inner > h1.entry-title::text")
        .get()
        .strip(),
        timestamp=selector.css(
            "div.entry-header-inner > ul > li.meta-date::text"
        ).get(),
        writer=selector.css(
            "div.entry-header-inner > ul span.author > a::text"
        ).get(),
        reading_time=int(
            selector.css(
                "div.entry-header-inner > ul > li.meta-reading-time"
            ).re(r"\d+")[0]
        ),
        summary=selector.css("div.entry-content > p")
        .xpath("string()")
        .get()
        .strip(),
        category=selector.css(
            "div.entry-header-inner a.category-style span.label::text"
        ).get(),
    )


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    BASE_URL = "https://blog.betrybe.com/"
    content = fetch(BASE_URL)
    next_page = scrape_next_page_link(content)
    news_urls = scrape_updates(html_content=content)
    while len(news_urls) < amount:
        content = fetch(next_page)
        news_urls.extend(scrape_updates(html_content=content))
        next_page = scrape_next_page_link(content)

    news = [scrape_news(fetch(url)) for url in news_urls][:amount]
    create_news(news)
    return news
