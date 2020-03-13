# -*- coding: utf-8 -*-
from logger.logger import crawler_logger as log
from crawler.crawler import Crawler

class worldometer(Crawler):
    def updateData(self):
        log.debug('[Func] worldometer.crawler')