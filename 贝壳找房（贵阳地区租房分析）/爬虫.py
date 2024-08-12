import requests
import re
import csv
from bs4 import BeautifulSoup


def get_page_one(url):
    headers = {
        'Cookie': 'select_city=520100; lianjia_uuid=4d5d6ba6-7909-4ff9-a3bf-f4a17bfdddf2; GUARANTEE_POPUP_SHOW=true; GUARANTEE_BANNER_SHOW=true; lianjia_ssid=fdd3ca3f-b028-40d5-a49c-a9d6f8e7cea4; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNjMwODgxNDA2MjVjMjlmNjI5YWQ1MTMyNjYwMzMxM2QwNzZmNWYyZTZjNzBhZjdiZDhmZmZhYjAwOGMxMDc3ZmU4MTIyMjgzNDgwYzBiYWMzZjcwM2U2MTk3Y2FmMDJjNDAzNWVhNjEwNmU0MTI2NjgyYjhiYTU2MDcxYjBmODcxYzE4YzQzODMwMWIzMGQ1ZTc5YjFkODkyMzkxNDVlNDg4YzU0NTgyZjBlNGI3YWJjYTUwZGYyZmYxMmQ1NWFmNTkwMWE5NzE2ZDNjZTdiZGZlZmJjNjhlNTk4Y2Q1MGVkMTViMjc3OGQ3Y2VhMDU0NGQ4ZTA4MzJlOGYyMGM2NFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2MDFlNmJlM1wifSIsInIiOiJodHRwczovL2d5Lnp1LmtlLmNvbS96dWZhbmciLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text

    # 2. 解析数据
    soup = BeautifulSoup(html, 'html.parser')
    div_list = soup.select('#content > div.content__article > div.content__list > div > div')
    pattern_1 = r'(\d+\.\d+㎡)'
    pattern_2 = r'(\d+室\d+厅\d+卫)'
    with open('贝壳数据.csv', 'a', encoding='utf-8') as file:
        for x in div_list:
            house_xingxi = x.select_one('.twoline').text
            score = x.select_one('p.content__list--item--des > a').text
            house_pingfang = re.findall(pattern_1, str(x))
            house_fangjian = re.findall(pattern_2, str(x))
            house_pingfang_str = ''.join(house_pingfang)
            house_fangjian_str = ''.join(house_fangjian)
            house_money = x.select_one('div > span').text
            writer = csv.writer(file)
            writer.writerow([house_xingxi, score, house_pingfang_str, house_fangjian_str, house_money])
            print(house_xingxi, score, house_pingfang_str, house_fangjian_str, house_money)
        writer.writerow([house_xingxi, score, house_pingfang_str, house_fangjian_str, house_money])

for index in range(0, 200):
    url = f"https://gy.zu.ke.com/zufang/pg{index}/#contentList"
    get_page_one(url)
