import requests
from bs4 import BeautifulSoup

from sources import SOURCES


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

    print("网页标题：", soup.title.text.strip())
