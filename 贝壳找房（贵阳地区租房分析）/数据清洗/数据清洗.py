# import csv
# import requests
# import re
# from bs4 import BeautifulSoup
# def get_page_one(url):
#     headers = {
#         'cookie':'lianjia_uuid=4d5d6ba6-7909-4ff9-a3bf-f4a17bfdddf2; select_city=520100; GUARANTEE_POPUP_SHOW=true; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNjMwODgxNDA2MjVjMjlmNjI5YWQ1MTMyNjYwMzMxM2RkYzQzYWE2NTVkZjNlYjYyYzdmODEwMjNmMzU5Yjk3ZTNhNmQwYmJiMzE0ZWFmM2MwZjUwOTMyNTViNjA4YjJmM2M5MmZjYTAxY2RkZWNkOWJiYmMwN2ViMDEyMTU1NGM2M2ZjYTZjNDQ2NDI3N2JiNjEzY2JhNDBkYjJmODNjMTdjODJmNDAyOTg4NmE3ZjNhN2FlZWE1YmNjNzZhZDdlNWExM2U3MzhkNzRlMmI1Y2E4ZWJiZTdmNmNmNDdhOTEwNGEzNjVmN2FkNzNkOTY3MWNiZGJjYjViMmYxNDZhZlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwYmNlMmZjNlwifSIsInIiOiJodHRwczovL2d5Lnp1LmtlLmNvbS96dWZhbmcvcGcxMDEvI2NvbnRlbnRMaXN0Iiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
#     }
#     response = requests.get(url, headers=headers)
#     html = response.text
#     # 2. 解析数据
#     soup = BeautifulSoup(html, 'html.parser')
#     div_list = soup.select('#content > div.content__article > div.content__list > div > div')
#     pattern = r'\d+\.\d+㎡'
#     pattern_1 = r'(\d+室\d+厅\d+卫)'
#     with open('贝壳信息.csv', 'w', encoding='utf-8') as file:
#         for x in div_list:
#             move_name = x.select_one('.twoline').text
#             score = x.select_one('#content > div.content__article > div.content__list > div > div > p.content__list--item--des > a').text
#             house_pingfang = re.findall(pattern, str(x))
#             house = re.findall(pattern_1,str(x))
#             house_pingfang_str =''.join(house_pingfang)
#             house_str = ''.join(house)
#             zu = x.select_one('.content__list--item-price').text
#             writer = csv.writer(file)
#             print(move_name,score,house_pingfang_str,house_str,zu)
#             writer.writerow([move_name, score, house_pingfang_str, house_str, zu])  # 写入数据
#
# for index in range(500):
#     url = f"https://gy.zu.ke.com/zufang/pg{index}/#contentList"
#     get_page_one(url)



#数据清洗
import pandas as pd
import re

# 加载CSV文件到DataFrame
file_path = '贝壳信息.csv'  # 请替换为您的文件路径
df = pd.read_csv(file_path, encoding= 'gbk')

# 显示DataFrame的前几行以了解其结构
df_head = df.head()

# 定义一个函数从字符串中提取数值
def extract_numerical_value(text):
    # 检查输入是否为字符串
    if not isinstance(text, str):
        return None

    # 在文本中查找所有数值模式
    numbers = re.findall(r'\d+', text)
    if numbers:
        # 将第一个数值模式转换为浮点数
        return float(numbers[0])
    return None

# 对Area和Rent列应用函数以提取数值
df['Area'] = df['Area'].apply(extract_numerical_value)
df['Rent'] = df['Rent'].apply(extract_numerical_value)

# 删除租金小于500或大于5000，以及面积为NaN和小于50平方的行
df_cleaned = df.dropna(subset=['Rent', 'Area'])  # 首先删除租金或面积为NaN的行
df_cleaned = df_cleaned[(df_cleaned['Rent'] >= 500) & (df_cleaned['Rent'] <= 5000) & (df_cleaned['Area'] >= 50)]

#将特殊字符替换为空
df_cleaned = df_cleaned.replace('\n', '', regex=True)
print(df_cleaned.head())
# 保存清洗后的文件
df_cleaned.to_csv("贝壳信息2.csv", index=False)
df_cleaned.head()
