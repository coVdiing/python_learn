# coding:UTF-8
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get('https://www.douban.com/',headers=headers)
print(r.status_code)