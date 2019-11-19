import requests
from bs4 import BeautifulSoup

############### 获取 html 及转码 ############################

base_url = 'http://mysql.taobao.org'
response = requests.get(base_url + '/monthly')

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

# print(month_list)
# print(month_dict)


all_list = []
all_dict = {}
for i in month_dict:
    ret = requests.get(month_dict[i])
    ret.encoding = 'utf-8'
    soup2 = BeautifulSoup(ret.text, 'html.parser')
    lis = soup2.body.div.contents[3].ul.find_all('a')

    for i in lis:
        str = ''
        str = str.join(i.string.strip())
        all_list.append(str)

        url = ''
        url = url.join(i.get('href').strip())
        url = base_url + url
        all_dict[str] = url

# print(all_list)
# print(all_dict)

for i in all_dict:
    # if('log' in i):
    # if('临时表那些事儿' in i):
    if('runcate undo log' in i):
        print(all_dict[i], end='')
        print('   ' + i)