from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):                          #定义url的异常处理函数
    try:
        html = urlopen(url)                 #网页在服务器上不存在
    except HTTPError:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        title = bsObj.body.h1
    except AttributeError:                  #处理网页标签错误
        return None

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
print(title)
if title == None:                           #分情况输出
    print("Title could not be found") 
else:
    print(title)  
