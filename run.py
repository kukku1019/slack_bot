#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackbot.bot import Bot
from plugins import bitbank
import concurrent.futures

def main():
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    bot = Bot()
    # bitbank.bitbankstart()
    tast = [executor.submit(bot.run()), executor.submit(bitbank.bitbankstart())]
    executor.shutdown()

if __name__ == "__main__":
    main()
