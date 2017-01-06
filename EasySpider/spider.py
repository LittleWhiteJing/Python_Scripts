#coding=utf-8
import re,os
import urllib
import urllib2

class Spider:
	def __init__(self,url):
		self.siteUrl = url
		self.dataDir = '/home/darkblue/workspace/data/'
	#获取整个页面
	def getPage(self):
		request = urllib2.Request(self.siteUrl)
		response = urllib2.urlopen(request)
		return response.read()
	#获取页面图片
	def getImg(self):
		page = self.getPage()
		regular = r'<img.*?src=".*?".*?/>'
		pattern = re.compile(regular)
		items = re.findall(pattern,page)
		return items
	def getInfo(self):
		page = self.getPage()
		regular = r'<li class=".*?">.*?</li>'
		items = re.findall(regular,page)
			for item in items:
				item.decode('ascii')
				print item+"\n"
		return items
	#下载整个页面
	def putPage(self,filename):
		os.chdir(self.dataDir)
		file = self.getPage()
		f = open(filename,'wb').write(file)
		return "download finished!"
			
url = raw_input("input the website url:")

#fname = raw_input("input the file name:")

spider = Spider(url)

items = spider.getInfo()

#print items

#info = spider.putPage(fname)

#print "info"

