import json
import requests

def searchPakage():
    packageNum = input('请输入运单号码：')
    url = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text='+ packageNum
    company = json.loads(requests.get(url).text)['auto'][0]['comCode']
    url2 = 'http://www.kuaidi100.com/query?type=' + company + '&postid=' + packageNum
    result = json.loads(requests.get(url2).text)['data']#[0]['context']
    for dic in result:
        print(dic['time']+':'+dic['context'])
while True:
    searchPakage()