# -*- coding: utf-8 -*-
import datetime
import logging

log_filename = datetime.datetime.now().strftime("log/covid19crawler_%Y-%m-%d.log")
log_console_format = '%(name)-7s: %(levelname)-5s %(message)s'
log_file_format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.DEBUG,
                    format=log_file_format,
                    datefmt='%m-%d %H:%M',
                    filename=log_filename)

# Set handler for sys.stderr
formatter = logging.Formatter(log_console_format)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Set logger for each module
cmd_logger = logging.getLogger('cmd')
config_logger = logging.getLogger('config')
crawler_logger = logging.getLogger('crawler')