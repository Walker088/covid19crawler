# -*- coding: utf-8 -*-

from logger.logger import config_logger as log
import os
import yaml

config_file_path = '{}/config/config.yaml'.format(os.getcwd())
data_storage_path = '{}/data'.format(os.getcwd())

class Config():
    '''
    Config class of corid19crawler
    '''
    def __init__(self):
        with open(config_file_path, 'r') as stream:
            self.conf = yaml.load(stream, Loader=yaml.FullLoader)
            self.auther = self.conf.get('owner', 'no owner found').get('name', 'no name found')
            self.auther_mail = self.conf.get('owner', 'no owner found').get('email', 'no email found')
            self.project_name = self.conf.get('project_name', 'no project name found')
            self.data_sources = self.conf.get('data_sources', 'no data sources found')

    def get_project_info(self):
        return {"auther": self.auther, "email": self.auther_mail,
                "project": self.project_name, "data sources": list(self.data_sources.keys())}

    def get_data_sources(self):
        return list(self.data_sources.keys())

    def get_source_url(self, source):
        if self.data_sources.get(source, 'Null') != 'Null':
            return self.data_sources.get(source, 'Null').get('url', 'Null')
        return []

    def get_data_storage_path(self):
        return data_storage_path
