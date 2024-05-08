# import requests



# API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/88f7cfa8064f3bd6319ba80fcbff9ace/ai/run/"
# headers = {"Authorization": "Bearer az1j5vpQdNVDzHFifWE0VOBeWTyhupLIDWOfuqYq"}


# def run(model, inputs):
#     input = { "messages": inputs }
#     response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
#     return response.json()


# inputs = [
#     { "role": "system", "content": "你是一个Python编程方面的专家" },
#     { "role": "user", "content": "怎么使用爬虫爬取到王者荣耀的英雄列表?请使用中文回答"}
# ]
# output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
# print(output)




import requests
from lxml import etree

# 发送请求获取英雄详情
url = "https://pvp.qq.com/web201605/herodetail/105.shtml"
response = requests.get(url)
response.encoding = "gbk"

# 解析HTML内容
html = etree.HTML(response.text)
# 获取/html/body/div[3]/div[1]/div/div/div[1]/ul/li[1]/span/i 的css属性
sc = html.xpath("//i[@class='ibar']/@style")
# 打印英雄属性
print(sc)
