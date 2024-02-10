#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from os import getenv

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = getenv("BOT_TOKEN")
    API_ID = getenv("API_ID")
    API_HASH = getenv("API_HASH")
    AUTH_USERS = getenv("AUTH_USERS")

