from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")                 #网页在服务器上不存在
bsObj = BeautifulSoup(html.read(),'html.parser')
namelist = bsObj.findAll("span",{"class","green"},text='the prince')    #findALL（tagName"标签"，tagAttributes{标签属性},text='指定文本'）
for name in namelist:
    print(name.get_text())