#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackbot.bot import Bot
from plugins import bitbank

def main():
    bot = Bot()
    bitbank.bitbankStart()
    bot.run()


if __name__ == "__main__":
    main()
