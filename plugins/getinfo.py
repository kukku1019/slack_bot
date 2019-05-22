#!/usr/bin/env python
# utf-8

import urllib.request
import json
import urllib.parse


# https://docs.bitbank.cc/#/
#  "{\"success\":1,\"data\":{\"sell\":\"1684999\",\"buy\":\"1683033\",\"high\":\"1754980\",\"low\":\"1526399\",\"last\":\"1682988\",\"vol\":\"258.7837\",\"timestamp\":1514801097122}}"

# レスポンス
# sell 現在の売り注文の最安値
# buy 現在の買い注文の最高値
# high 過去24時間の最高値取引価格
# low 過去24時間の最安値取引価格
# last 最新取引価格
# vol 過去24時間の出来高

class getinfo(object):
    def __init__(self, pair_list, bitbank_public):
        self.bitbank_public = bitbank_public
        self.pair_list = pair_list

    # 取引情報単体
    def get(self, pair):
        ticker = "/" + pair + "/ticker"
        info = urllib.request.urlopen(self.bitbank_public + ticker)
        info_decode = info.read().decode("utf-8")
        return info_decode

    # 取引情報全部
    def get_all(self):
        all = {}
        for index in range(len(self.pair_list)):
            data_json = self.get(self.pair_list[index])
            data_dict = json.loads(data_json)  # data_dict 辞書型
            all[self.pair_list[index]] = data_dict
        return all

    # レスポンス
    #  asks 売り板 [価格, 数量]
    #  bids 買い板 [価格, 数量]
    # 取引数 値段
    def depth(self, pair):
        ticker = "/" + pair + "/depth"
        info = urllib.request.urlopen(self.bitbank_public + ticker)
        info_decode = info.read().decode("utf-8")
        return info_decode

    def depth_all(self):
        all = {}
        for index in range(len(self.pair_list)):
            data_json = self.depth(self.pair_list[index])
            data_dict = json.loads(data_json)  # data_dict 辞書型
            all[self.pair_list[index]] = data_dict
        return all
