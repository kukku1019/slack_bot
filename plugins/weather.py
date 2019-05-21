#encoding:utf-8
import urllib.request, urllib.error, sys
import json
from slackbot.bot import respond_to

try: citycode = sys.argv[1]
except: citycode = '130010' #デフォルト地域
resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

# 読み込んだJSONデータをディクショナリ型に変換
resp = json.loads(resp)


@respond_to('天気')
def mention_func(message):
    message.send('**************************') # メンション
    message.send(resp['title']) # メンション
    message.send('**************************') # メンション
    message.send(resp['description']['text']) # メンション

    for forecast in resp['forecasts']:
        message.send ('**************************')
        message.send (forecast['dateLabel']+'('+forecast['date']+')')
        message.send (forecast['telop'])
    message.send ('**************************')
