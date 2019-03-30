#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import urllib
#urllib2使用GET方式的请求
url = 'http://www.baidu.com/s'
values = {'wd' : '车云'}
# 必须编码
data = urllib.urlencode(values)
url = url + '?' + data
print url
#url == http://www.baidu.com/s?wd=%E8%BD%A6%E4%BA%91
#创建request对象
request = urllib2.Request(url)
#发送请求，获取结果
try:
 response = urllib2.urlopen(request)
except BaseException, err:
 print err
 exit()
#获取状态码，如果是200表示获取成功
code = response.getcode()
print code
#读取内容
if 200 == code:
 content = response.read()
 print content