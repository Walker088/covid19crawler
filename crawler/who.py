# -*- coding: utf-8 -*-
from logger.logger import crawler_logger as log
from crawler.crawler import Crawler

from tqdm import tqdm
import pandas as pd
import datetime

class who(Crawler):
    def __init__(self, base_dir, source_name, source_urls):
        self.base_dir = base_dir
        self.source_name = source_name
        self.source_urls = source_urls

    def get_file_name(self, url):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        return '{}/{}/{}-{}-{}'.format(self.base_dir, self.source_name,
                                    date, self.source_name, url.split('/')[-1])

    def updateData(self):
        #log.debug('[Func] who.crawler, source: %s,\n \
        #          urls %s' % (self.source_name, self.source_urls))
        urls_tqdm = tqdm(self.source_urls)
        for url in urls_tqdm:
            urls_tqdm.set_description("[who] Processing %s" % (url.split('/')[-1]))
            try:
                df = pd.read_csv(url)
                df.to_csv(self.get_file_name(url))
            except(Exception) as error:
                log.error('Connection to %s Failed' % (url))
                log.error(error)