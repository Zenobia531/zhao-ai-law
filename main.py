import requests

print("赵律AI法律内容中心启动成功！")

url = "https://www.court.gov.cn"

try:
    response = requests.get(url, timeout=10)
    print("网站访问成功：", response.status_code)
except Exception as e:
    print("访问失败：", e)
