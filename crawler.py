from dataclasses import dataclass
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


@dataclass
class Article:
    """统一的文章数据格式。"""

    title: str
    url: str
    source_name: str
    publish_time: Optional[str] = None
    summary: Optional[str] = None


def fetch_page_title(url: str) -> str:
    """访问网页并提取网页标题，用于验证采集功能。"""

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/131.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    if soup.title and soup.title.string:
        return soup.title.string.strip()

    return "未提取到网页标题"
    
def download_html(url):
    import requests

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        )
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=20,
    )

    response.raise_for_status()

    return response.text

def parse_court_article_list(
    html: str,
    source_name: str,
    source_url: str,
) -> list[Article]:
    """解析最高人民法院栏目页中的文章列表。"""

    soup = BeautifulSoup(html, "html.parser")
    article_list = soup.find("div", class_="sec_list")

    if article_list is None:
        return []

    articles: list[Article] = []

    for item in article_list.find("ul").find_all("li", recursive=False):
        link_tag = item.find("a")
        date_tag = item.find("i", class_="date")

        if link_tag is None:
            continue

        article = Article(
            title=link_tag.get_text(strip=True),
            url=urljoin(source_url, link_tag.get("href", "")),
            source_name=source_name,
            publish_time=(
                date_tag.get_text(strip=True)
                if date_tag is not None
                else None
            ),
        )

        articles.append(article)

    return articles