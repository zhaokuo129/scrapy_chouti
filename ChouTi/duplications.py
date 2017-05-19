
#自定义去重
class RepeatFilter(object):
    def __init__(self):
        self.visited_urls = set()   #创建集合

    @classmethod
    def from_settings(cls, settings):
        '''
        初始化时，调用
        :param settings:
        :return:
        '''
        return cls()    #实例化类

    def request_seen(self, request):
        '''
        检测当前请求是否已经被访问过
        :param request:
        :return: True表示已经访问过；False表示未访问过
        '''
        if request.url in self.visited_urls:#如果在返回True，不在加到集合中
            return True
        self.visited_urls.add(request.url)
        return False

    def open(self):  # can return deferred
        '''
        开始爬去请求时，调用
        :return:
        '''
        pass

    def close(self, reason):  # can return a deferred
        '''
        结束爬虫爬取时，调用
        :param reason:
        :return:
        '''
        pass

    def log(self, request, spider):  # log that a request has been filtered
        '''
        记录日志
        :param request:
        :param spider:
        :return:
        '''
        pass