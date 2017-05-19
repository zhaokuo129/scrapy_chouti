# -*- coding: utf-8 -*-
import scrapy
import io
import sys
import requests
# from scrapy.dupefilter import RFPDupeFilter
from scrapy.http import Request
from ..items import ChoutiItem
from scrapy.selector import Selector,HtmlXPathSelector
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class ChoutiSpider(scrapy.Spider):
    name = "chouti"
    allowed_domains = ["chouti.com"]
    start_urls = ['http://dig.chouti.com/']

    #可从写start_requests修改起始调用的回调函数
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url,callback=self.get_img)

    def parse(self, response):
        print(response.url)
        news_item_hxs = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]')  # 标签对象列表
        for item in news_item_hxs:
            url = item.xpath('.//img/@original').extract_first()
            img_url = 'http:%s' % url
            img_content = requests.get(url=img_url).content
            url_prefix,file_name = img_url.rsplit('/',1)
            item_obj = ChoutiItem(img_url=img_url, file_name=file_name,content=img_content)
            # 将item对象传递给pipeline
            yield item_obj
        page_hxs = Selector(response=response).xpath('//a[re:test(@href, "/all/hot/recent/\d+")]/@href').extract()
        for url in page_hxs:
            url = "http://dig.chouti.com%s" % url
            # 将新要访问的url添加到调度器
            yield Request(url=url, callback=self.parse)