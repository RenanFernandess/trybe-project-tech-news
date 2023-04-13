import time
import requests
import parsel


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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
