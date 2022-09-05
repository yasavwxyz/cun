# Copyright (C) 2020-2022 by yasavwxyz@Github, < https://github.com/yasavwxyz >.
#
# This file is part of < https://github.com/yasavwxyz/cun > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/yasavwxyz/cun/blob/master/LICENSE >
#
# All rights reserved.

from . import cli

filter = cli["cun"]["FILTER"]


async def add_filters(keyword, chat_id, message_id) -> None:
    add = await filter.find_one({"keyword": keyword})
    if add:
        await filter.update_one(
            {"keyword": keyword},
            {"$set": {"chat_id": chat_id, "msg_id": message_id}},
        )
    else:
        await filter.insert_one(
            {"keyword": keyword, "chat_id": chat_id, "msg_id": message_id}
        )


async def del_filters(keyword, chat_id):
    await filter.delete_one({"keyword": keyword, "chat_id": chat_id})


async def filters_info(keyword, chat_id):
    r = await filter.find_one({"keyword": keyword, "chat_id": chat_id})
    if r:
        return r
    else:
        return False


async def filters_del(chat_id):
    await filter.delete_many({"chat_id": chat_id})


async def all_filters(chat_id):
    r = [jo async for jo in filter.find({"chat_id": chat_id})]
    if r:
        return r
    else:
        return False