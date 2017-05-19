# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ChoutiPipeline(object):
    def __init__(self, v):
        self.value = v

    def process_item(self, item, spider):
        '''
        每当数据需要持久化时，就会被调用
        :param item:
        :param spider:
        :return:
        '''
        file_path = os.path.join(BASEDIR,'ChouTi','img',item['file_name'])
        with open(file_path,'wb') as f:
            f.write(item['content'])

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        val = crawler.settings.getint('MMMM')
        return cls(val)

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        例如:写文件：如果同时写入一个文件中，没必要每一次都打开一次，文件，可以开始的时候打开一次，结束后关闭
        例如:数据库连接
        :param spider:
        :return:
        """
        pass

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        pass

# class XiaohuaPipeline(object):
#     def process_item(self, item, spider):
#         file_path = os.path.join(BASEDIR,'ChouTi','img',item['file_name'])
#         with open(file_path,'wb') as f:
#             f.write(item['content'])
