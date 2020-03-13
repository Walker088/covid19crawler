# -*- coding: utf-8 -*-
from logger.logger import crawler_logger as log
from crawler.crawler import Crawler

from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import pandas as pd
import requests
import datetime

class worldometer(Crawler):
    def __init__(self, base_dir, source_name, source_urls):
        self.base_dir = base_dir
        self.source_name = source_name
        self.source_urls = source_urls

    def get_file_name(self, url):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        return '{}/{}/{}-{}.csv'.format(self.base_dir, self.source_name,
                                    date, self.source_name)

    def updateData(self):
        #log.debug('[Func] worldometer.crawler, source: %s,\n \
        #          urls %s' % (self.source_name, self.source_urls))
        urls_tqdm = tqdm(self.source_urls)
        for url in urls_tqdm:
            urls_tqdm.set_description("[worldometer] Processing %s" % (self.source_name))
            try:
                with requests.Session() as s:
                    headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) \
                                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
                    soup = bs(s.get(url, headers=headers).text, 'html.parser')
                    thead = soup.find(id='main_table_countries').find('thead').find_all('th')
                    tbody = soup.find(id='main_table_countries').find_all('tr')
                    head = [ e.text.replace(',', '/').strip('\"') for e in thead ]
                    data = list(filter(None, [ [e.text.strip() for e in row.find_all('td')] for row in tbody ]))
                    df = pd.DataFrame(data, columns=head)
                    df.to_csv(self.get_file_name(url))
            except(Exception) as error:
                log.error('Connection to %s Failed' % (url))
                log.error(error)