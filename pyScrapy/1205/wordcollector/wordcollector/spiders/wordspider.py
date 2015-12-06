#!/usr/bin/python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import os
import scrapy

# Python scrapy spider
# 
# Trying to collect words from websites

class WordSpider(scrapy.Spider):
    name = 'wordspider'
    allowd_domains = ['baidu.com','jianshu.com','slate.com']
    start_urls = [
            r'http://www.jianshu.com/p/078ad2067419',
            r'http://www.slate.com/articles/technology/technology/2013/06/how_people_read_online_why_you_won_t_finish_this_article.single.html'
            ]
    def parse(self,response):
        pass
        resultfolder = self.name+'_results'
        if not os.path.isdir(resultfolder):
            os.mkdir(resultfolder)
        

        print 'response url:',response.url
        folder = response.url.split('://')[1]
        filename = folder

        if folder.find(r'/') != -1:
            filename = folder.split(r'/')[1:]
            filename = '__'.join(filename)
            folder = folder.split(r'/')[0]

        # save page result to folder:
        folder = resultfolder +os.sep+folder
        if not os.path.isdir(folder):
            os.makedirs(folder)

        with open(folder+os.sep+filename,'wb') as fin:
            fin.write(response.body)

