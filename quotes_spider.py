# encoding=UTF-8
import scrapy
from urllib import urlencode


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        words = [u'三七', u'内科']
        for word in words:
            url = 'https://baike.baidu.com/item/%s?fr=aladdin' % word.encode('utf-8')
            yield scrapy.Request(url=url, callback=lambda response, word=word: self.parse(response, word))
            
        print 'finished -------------------------->'

    def parse(self, response, word):
        
        page = response.url.split("/")[-2]
        print '----------------------> %s' % word.encode('utf-8')
        file = open('txts/%s.txt' % word, 'w')
        #summary = response.css('.para::text')
        #summary = response.css('#content p::text')
        summary = response.xpath('//div[re:test(@class, "^para.*$")]').css('::text')
        #print summary.extract()
        for spt in summary.extract():
          file.write(spt.encode('utf-8'))