# Copyright (C) 2020-2022 by yasavwxyz@Github, < https://github.com/yasavwxyz >.
#
# This file is part of < https://github.com/yasavwxyz/cun > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/yasavwxyz/cun/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import idle, Client, filters
from config import PREFIX
from cun import app, LOGGER
import logging
from cun.modules import *

app.start()
me = app.get_me()
print(f"Zect UserBot started for user {me.id}. Type {PREFIX}help in any telegram chat.")
idle()