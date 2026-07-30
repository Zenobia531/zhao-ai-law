from turtle import title

import requests
from bs4 import BeautifulSoup

from sources import SOURCES

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

    response = requests.get(
        source["url"],
        headers=headers,
        timeout=20,
    )

    print("HTTP状态：", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    article_list = soup.find("div", class_="sec_list")
    #print(article_list)
   
    articles = article_list.find("ul").find_all("li", recursive=False)

    print("文章数量：", len(articles))

    for article in articles:
        link_tag = article.find("a")

        title = link_tag.text.strip()
        date = article.find("i", class_="date").text.strip()
        link = urljoin(source["url"], link_tag["href"])

        print(title)
        print(date)
        print(link)
        print("-" * 40)