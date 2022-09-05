# Copyright (C) 2020-2022 by yasavwxyz@Github, < https://github.com/yasavwxyz >.
#
# This file is part of < https://github.com/yasavwxyz/cun > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/yasavwxyz/cun/blob/master/LICENSE >
#
# All rights reserved.

from . import cli

collection = cli["cun"]["gmute"]


async def gmute_user(chat):
    doc = {"_id": "Gmute", "users": [chat]}
    r = await collection.find_one({"_id": "Gmute"})
    if r:
        await collection.update_one({"_id": "Gmute"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)

async def get_gmuted_users():
    results = await collection.find_one({"_id": "Gmute"})
    if results:
        return results["users"]
    else:
        return []

async def ungmute_user(chat):
    await collection.update_one({"_id": "Gmute"}, {"$pull": {"users": chat}})