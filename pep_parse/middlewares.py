from scrapy import signals


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        spider = cls()
        crawler.signals.connect(
            spider.spider_opened,
            signal=signals.spider_opened
        )
        return spider

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for item in result:
            yield item

    def process_start_requests(self, start_requests, spider):
        for request in start_requests:
            yield request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware(PepParseSpiderMiddleware):

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response
