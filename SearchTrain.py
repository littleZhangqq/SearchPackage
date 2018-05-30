"""
Usage:
    输入要查询的火车类型可以多选（动车d,高铁g,特快t,快速k,直达z）
    输入出发地、目的地、出发日期。
    查询结果以命令行形式自动呈现。

Examples：
    Please input the trainType you want to search :dgz
    Please input the city you want leave :南京
    Please input the city you will arrive :北京
    Please input the date(Example:2017-09-27) :2018-03-01
"""

#coding = utf-8

import json
import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
from Stations import station



class Mytrain:
    def __init__(self):
        self.trainOption = input('-d动车 -g高铁 -k快速 -t特快 -z直达,Please input the trainType you want to search :')
        self.fromstation = input('输入出发城市：')
        self.toStation = input('输入目标城市：')
        self.tripDate = input('输入出发日期，如:2017-09-27：')
        self.headers = {
            "Cookie":"自定义",
            "User-Agent":"自定义"
        }
        self.available_trains,self.options = self.searchTrain()


    @property

    def trains(self):
        for item in self.available_trains:
            cm = item.split('|')
            train_no = cm[3]
            inital = train_no[0].lower()
            if not self.options or inital in self.options:
                train = [
                    train_no,
                    '\n'.join(Fore.GREEN + cm[6] + Fore.RESET,
                              Fore.RED + cm[7]+Fore.RESET),
                    '\n'.join(Fore.GREEN + cm[8] + Fore.RESET,
                              Fore.RED + cm[9] + Fore.RESET),
                    cm[10],
                    cm[32],
                    cm[25],
                    cm[31],
                    cm[30],
                    cm[21],
                    cm[23],
                    cm[28],
                    cm[24],
                    cm[29],
                    cm[26],
                    cm[22]
                ]
                yield train


    def pretty_print(self):
        pt = PrettyTable()
        header = '车次 车站 时间 历时 商务座 特等座 一等 二等 高级软卧 软卧 硬卧 软座 硬座 无座 其他'.split()
        pt._set_feild_names(header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


    def searchTrain(self):
        arguments = {
            'option':self.trainOption,
            'from':self.fromstation,
            'to':self.toStation,
            'date':self.tripDate
        }

        from_station = station[self.fromstation]
        to_station = station[self.toStation]
        date = arguments[self.tripDate]
        url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(date, from_station,to_station)
        html = requests.get(url,headers = self.headers,veriify=False)
        avaelable_trains = html.json()['data']['result']
        return avaelable_trains


if __name__ == '__main__':
     while True:
         my = Mytrain()
         available = my.searchTrain()
         print(available)