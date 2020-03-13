#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logger.logger import cmd_logger as log
from config.config import Config

from argparse import ArgumentParser
from argparse import MetavarTypeHelpFormatter
from prettytable import PrettyTable
import traceback, sys

conf = Config()

def init_argparser():
    log.debug('[Func] init_argparser')
    desp = 'The crawler from which could download the online sources of covid19 data'
    parser = ArgumentParser(prog=None, description=desp, formatter_class=MetavarTypeHelpFormatter)
    parser.add_argument('-u', '--update', \
                        type=str, \
                        required=False, \
                        nargs='?', \
                        default='all', \
                        help='update covid19 data from source')
    parser.add_argument('-ls', '--list-source', \
                        action='store_true', \
                        default=False, \
                        help='show available covid19 data resourse')
    return parser.parse_args()

def printListSources():
    log.debug('[Func] printListSources')
    try:
        tb = PrettyTable()
        tb.field_names = ['Source Name', 'Source Url']
        for source in conf.get_data_sources():
            log.debug('source: %s' % conf.get_source_url(source))
            tb.add_row([source , '\n'.join(conf.get_source_url(source))])
        print(tb)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return None

def updatedata(source):
    log.debug('[Func] update single data(%s)' % source)
    for crawler in conf.get_crawlers():
        if source == crawler.__class__.__name__:
            crawler.updateData()

def updateData(source):
    log.debug('[Func] updateData(%s)' % source)
    if source != 'all':
        log.debug('update given source: %s' % source)
        if source not in conf.get_data_sources():
            log.error('source %s not exist' % source)
            sys.exit()
        updatedata(source)
    else:
        log.debug('update all sources')
        for source in conf.get_data_sources():
            updatedata(source)

def router():
    log.debug('[Func] router')
    args = init_argparser()
    log.debug(args)
    if args.list_source:
        printListSources()
    else:
        updateData(args.update)

if __name__ == '__main__':
    log.info('Welcom to covid19crawler ヽ(́◕◞౪◟◕‵)ﾉ')
    log.info(conf.get_project_info())
    router()