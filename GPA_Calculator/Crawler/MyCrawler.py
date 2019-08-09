import requests
import re
# from urllib import request

#  = "http://210.42.121.241/"
url = "https://www.yuyouge.com/book/2550/"
url_head = "https://www.yuyouge.com"
stu_id = ""
pswd = ""
res = requests.get(url)
html = res.text

ul = re.findall(r'<ul id="chapters-list" class="list-group-item">.*?</ul>',html,re.S)[0]
# 小说名称
title = re.findall(r'<meta property="og:title" content="(.*?)"/>',html,re.S)[0]
# 新建文件保存小说
# 每一章节url和名称
chapter_info_list = re.findall(r'href="(.*?)">(.*?)</a>',ul)
print(title)
# print(res.content)
#print(html)
#print(ul)
#print(chapter_info_list)