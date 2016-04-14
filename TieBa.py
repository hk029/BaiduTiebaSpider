#-*- coding:utf-8 -*-

import re
import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



BaseURL = 'http://tieba.baidu.com/mo/q---AE99FE88ABC9F3207919A03C71EE5165%3AFG%3D1--1-3-0--2--wapp_1460602606553_811/'


def spider(url):
    head = {'Referer':url,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    html = requests.get(url,headers = head)
    title = {}
    selector = etree.HTML(html.content)
    contents = selector.xpath('//div[@class="i"]')
    i = 0
    for each in contents:
        #print each
        content = each.xpath('a/text()')
        turl = each.xpath('a/@href')
        detail = each.xpath('p/text()')
        print content[0],detail[0]
        title[i] = BaseURL + turl[0]
        i +=1
    print ""
    GetReply(title[0])

def GetReply(url):

    head = {'Referer': url,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    html = requests.get(url,headers = head)
    selector = etree.HTML(html.content)
    contents = selector.xpath('//div[@class="i"]')
    for each in contents:
        #print each
        content = each.xpath('string(.)')
        print content

if __name__ == '__main__':
    url = BaseURL + 'm?word=KEYWORD&tn6=bdISP&tn4=bdKSW&tn7=bdPSB&lp=1050&sub4=%E8%BF%9B%E5%90%A7'
    text = raw_input('输入贴吧名：')
    url = re.sub('KEYWORD',text,url)

    url2 = 'http://tieba.baidu.com/p/4478543847'
    spider(url)
