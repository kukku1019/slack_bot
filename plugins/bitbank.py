#!/usr/bin/env python
# coding:utf-8
from plugins import getinfo
import json
from decimal import Decimal
import sys, time
import python_bitbankcc

# class run(object):
#
#     def __init__(self):
#         self.data=
if __name__ == "__main__":
    pair_list = ("btc_jpy", "xrp_jpy", "ltc_btc", "eth_btc",
                 "mona_jpy", "mona_btc", "bcc_jpy", "bcc_btc")
    bitbank = "https://public.bitbank.cc"

    while True:
        start = time.time()
        sum_asks = 0
        sum_bids = 0
        # 1~199
        range_dif = 50
        target = ""
        depth = getinfo(pair_list, bitbank).depth("mona_jpy")
        last = python_bitbankcc.public().get_ticker("mona_jpy")["last"]
        depth_json = json.loads(depth)
        depth_asks = depth_json["data"]["asks"]
        depth_bids = depth_json["data"]["bids"]
        for math in range(range_dif):
            # sum_asks = sum_asks + Decimal(depth_asks[math][1]) * Decimal(depth_asks[math][0])
            sum_asks = sum_asks + Decimal(depth_asks[math][1])
            # print(str(math) + " 値段: " + str(depth_list[math][0]) + " 量: " + str(depth_list[math][1]) + " 総額:" + str(Decimal(depth_list[math][1]) * Decimal(depth_list[math][0])))

        for math in range(range_dif):
            # sum_bids = sum_asks + Decimal(depth_bids[math][1]) * Decimal(depth_bids[math][0])
            sum_bids = sum_asks + Decimal(depth_bids[math][1])
        if (sum_asks - sum_bids) > 0:
            target = "上昇"
        elif (sum_bids - sum_asks) > 0:
            target = "降下"
        else:
            target = "エラー"
        sys.stdout.write(
            "\r" + target + "　最新値段：" + last + "　買う数:" + str(sum_asks) + " 売る数" + str(sum_bids) + " timelag:" + str(
                start - time.time())
            )
        sys.stdout.flush()
        time.sleep(2)