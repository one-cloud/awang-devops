# -*- coding: utf-8 -*-
# @Author: awang
# @Date:   2020-03-11 07:50:05 
# @Last Modified by:   awang
# @Last Modified time: 2020-04-07 20:40:33

import requests
import time
import re

def DownPic(PicNum):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    PicUrl = 'https://bing.ioliu.cn/ranking?p=' + str(PicNum)
    conntent = requests.get(PicUrl, headers=headers)
    response = conntent.text
    ReResponse = re.compile(r'pic=(.*?)imageslim')
    PicList = re.findall(ReResponse, response)
    return PicList



if __name__ == '__main__':
    for num in range(1,20,1):
        for i in DownPic(num):
            url = i.strip('?')
            print(url)
            html = requests.get(url)
            #print(html)
            picname = 'pic/' + str(time.time()) + '.jpg'
            print(picname)
            with open(picname, 'wb') as file:
                file.write(html.content)
            print('阿旺壁纸%s下载完成!' %picname)




