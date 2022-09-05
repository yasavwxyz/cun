# Copyright (C) 2020-2022 by yasavwxyz@Github, < https://github.com/yasavwxyz >.
#
# This file is part of < https://github.com/yasavwxyz/cun > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/yasavwxyz/cun/blob/master/LICENSE >
#
# All rights reserved.


import motor.motor_asyncio
from config import MONGO_URI

cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
