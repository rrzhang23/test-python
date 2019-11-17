import requests
from bs4 import BeautifulSoup

############### 获取 html 及转码 ############################

base_url = 'http://mysql.taobao.org/monthly/2019/09/'
response = requests.get(base_url)

# print(response.content.decode('utf-8'))

# 同上
print('response.encoding : ' + response.encoding)
print('response.apparent_encoding : ' + response.apparent_encoding)
response.encoding = response.apparent_encoding
print('after set encoding, response.encoding : ' + response.encoding)
# print(response.text)
##########################################################


soup = BeautifulSoup(response.text, 'html.parser')
print(type(soup.body.div.contents[3].ul.find_all('a')))
# print(soup.body.div.contents[3].ul.find_all('a'))

# 所有 <li> tag
lis = soup.body.div.contents[3].ul.find_all('a')
month_list = []
month_dict = {}
for i in lis:
    # print(i.string.strip())
    str = ''
    str = str.join(i.string.strip())
    month_list.append(str)

    url = ''
    url = url.join(i.get('href').strip())
    url = base_url + url
    month_dict[str] = url

print(month_list)
print(month_dict)