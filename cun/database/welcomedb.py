# Copyright (C) 2020-2022 by yasavwxyz@Github, < https://github.com/yasavwxyz >.
#
# This file is part of < https://github.com/yasavwxyz/cun > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/yasavwxyz/cun/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.filters import chat
from . import cli

collection = cli["cun"]["welcome"]


async def save_welcome(chat_id, msg_id):
    doc = {"_id": 1, "welcomes": {chat_id: msg_id}}
    result = await collection.find_one({"_id": 1})
    if result:
        await collection.update_one(
            {"_id": 1}, {"$set": {f"welcomes.{chat_id}": msg_id}}
        )
    else:
        await collection.insert_one(doc)


async def get_welcome(chat_id):
    result = await collection.find_one({"_id": 1})
    if result is not None:
        try:
            msg_id = result["welcomes"][chat_id]
            return msg_id
        except KeyError:
            return None
    else:
        return None


async def clear_welcome(chat_id):
    await collection.update_one({"_id": 1}, {"$unset": {f"welcomes.{chat_id}": ""}})