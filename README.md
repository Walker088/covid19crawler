# covid19crawler
A Crawler to download the live number of cases in the world.

# Quick Start
## Local Env
```bash
# create virtual env
$ py3 -m venv venv
# install the dependency packages
$ source ./venv/bin/activate
$ pip3 install -r requirements.txt
# update data
$ py3 cmd.py
# list data sources
$ py3 cmd.py -ls
# show help msg
$ py3 cmd.py -h

# after development
$ pip3 freeze > requirements.txt
```

# Data Sources
- [Coronavirus Source Data – WHO Situation Reports](https://ourworldindata.org/coronavirus-source-data)
- [Worldometer](https://www.worldometers.info/coronavirus/)