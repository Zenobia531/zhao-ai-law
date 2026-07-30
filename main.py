from crawler import fetch_page_title


def main() -> None:
    url = "https://www.court.gov.cn"

    print("赵律AI法律内容中心启动成功！")
    print("正在访问：", url)

    try:
        title = fetch_page_title(url)
        print("网页标题：", title)
        print("采集模块运行成功！")
    except Exception as exc:
        print("采集模块运行失败：", exc)
        raise


if __name__ == "__main__":
    main()
