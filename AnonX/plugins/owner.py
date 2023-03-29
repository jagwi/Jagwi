from pyrogram 
import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app 

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 



@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIDG2QhN85PjxC3IZl3hYefSbz_w60-AAI-CQAC5Nr5V3U6V4xWQpckLwQ")

    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""ʜᴇʏ ʙᴀʙʏ🖤\n\nʜᴇʀᴇ ɪs ʙᴏᴛ ʀᴇᴘᴏ 💞""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )


