import re
import requests
import urllib3
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
urllib3.disable_warnings()
html = requests.get(url)

station = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', html.text)
pprint(station,indent=4)