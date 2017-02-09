#coding=utf-8
#自动登陆
import urllib2,urllib,cookielib

host_url = "https://www.douban.com/"#所在url
login_url = "https://www.douban.com/accounts/login"#登录请求url

#设置cookie处理器，负责从服务器下载cookie到本地，在发送请求时带上本地cookie
cj = cookielib.LWPCookieJar()#初始化一个cookie实例
cookie_support = urllib2.HTTPCookieProcessor(cj)#创建存放cookie的容器
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)#自定义opener，将其与cookie对象绑定
urllib2.install_opener(opener)#安装opener，此后调用urlopen()时都会使用安装过的opener对象

#在调用urllib2.urlopen(url)的时候，其实urllib2在open函数内部创建了一个默认的opener对象。然后调用opener.open()函数
h = urllib2.urlopen(host_url)

#设置headers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
			'Referer':'https://www.douban.com/'}

#data 抓包获取，得知需要post的内容
data = {'source':'index_nav',
		'form_email':'',#账号
		'form_password':''}#密码

postData = urllib.urlencode(data)

request = urllib2.Request(login_url,postData,headers)
print request
reponse = urllib2.urlopen(request)
print reponse.code#响应码
text = reponse.read()
print text