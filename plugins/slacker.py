#!/usr/bin/env python
# utf-8

# from slacker import Slacker
import slackbot_settings as setting
from slacker import Slacker


class slacker(object):
    def __init__(self):
        self.mesBot = Slacker(setting.API_TOKEN)
        self.channel = '#bitbank_チャンネル'

    def sendMessage(self,message):
        return self.mesBot.chat.post_message(self.channel,message)
