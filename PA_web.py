# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:46:20 2017

@author: yuguang
"""
#import requests as re
#import os
from bs4 import BeautifulSoup
import requests
import re
##Websites are the API
#r = re.get("http://www.baidu.com")
#print(r.status_code)
#r.enconding = 'utf-8'
#print(r.text)

#爬虫程序1
#def getHTMLText(url):
#    try:
#        r = re.get(url, timeout = 30)
#        r.raise_for_status() #如果不是200，引发HTTPError异常
#        r.encoding = r.apparent_encoding
#        return r.text
#    except:
#        return "产生异常"
#        
#if __name__ == "__main__":
#    url = "http://www.baidu.com"
#    print(getHTMLText(url))

##爬取京东
#url = "https://item.jd.com/2967929.html"
#try:
#    r = re.get(url)
#    r.status_code
#    r.encoding = r.apparent_encoding
#    print(r.text[:10000])
#except:
#    print("爬取失败")

##爬取亚马逊
#url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
#
#try:
#    kv = {'user-agent':'Mozilla/5.0'}
#    r = re.get(url, headers = kv)
#    print(r.status_code)
#    r.encoding = r.apparent_encoding
#    #print(r.encoding)
#    print(r.request.headers) 
#    #print(r.text[:5000])
#except:
#    print("爬取失败")

##挖关键字
#url = "https://www.baidu.com"
#
#try:
#    kv = {'wd':'Python'}
#    r = re.get(url, params = kv)
#    #print(r.status_code)
#    r.raise_for_status()
#    #r.encoding = r.appare nt_encoding
#    #print(r.encoding)
#    print(len(r.text)) 
#    #print(r.text[:5000])
#except:
#    print("爬取失败")

##爬取图片。 新建文件夹令文件在新文件夹中生成，需要在路径后面添加／
#root = "/Users/yuguang/Desktop/python3/python/"
#url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
#path = root + url.split('/')[-1]
#try:
#    if not os.path.exists(root):
#        os.mkdir(root)
#    #path = root+url.split('/')[-1]
#    if not os.path.exists(path):
#        r = re.get(url)
#        with open(path, 'wb') as f:
#            f.write(r.content) 
#            f.close()
#        print("文件保存成功")
#    else:
#        print("文件已存在")
#except:
#    print("爬取失败")

##爬取ip地址
#url = "http://m.ip138.com/ip.asp?ip="
#try:
#    r = re.get(url+'14.215.177.39')
#    print(r.status_code)
#    r.raise_for_status
#    r.encoding = r.apparent_encoding
#    print(r.text[-500:])
#except:
#    print("false")

##beautifulsoup可解析代码,正则表达式，找到以link开头，但不完全为link 的表达式信息。正则表达式：搜索值的一部分即可实现
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
##print(r.text)
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.find_all(id=re.compile('link')))

#print(soup.a.name)
#tag = soup.a
#print(tag.attrs['class'])
#print(soup.a.parent.name)
#print(soup.a)
