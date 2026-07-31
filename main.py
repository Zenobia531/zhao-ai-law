from turtle import title

from sources import SOURCES
from crawler import parse_court_article_list, download_html

from urllib.parse import urljoin


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


for source in SOURCES:
    if not source["enabled"]:
        continue

    print("=" * 60)
    print(source["name"])
    print(source["column"])
    print(source["url"])

    html = download_html(source["url"])

    print("网页下载成功")

articles = parse_court_article_list(
    html=html,
    source_name=source["name"],
    source_url=source["url"],
)

print("文章数量：", len(articles))

for article in articles:
    print(article.title)
    print(article.publish_time)
    print(article.url)
    print("-" * 40)