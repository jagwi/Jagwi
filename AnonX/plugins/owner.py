from pyrogram import Client, filters
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
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ʙᴜɪʟᴅɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ʙᴜɪʟᴅɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ʙᴜɪʟᴅɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ʙᴜɪʟᴅɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(

"CAACAgUAAxkBAAIDG2QhN85PjxC3IZl3hYefSbz_w60-AAI-CQAC5Nr5V3U6V4xWQpckLwQ")
    await umm.delete()
    await asyncio.sleep(2)
    await m.reply_photo(
        photo=f"https://te.legra.ph/file/01c4b8a952caa98ae077d.jpg",
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



@app.on_message(
    filters.command("ping")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("💥")
    await asyncio.sleep(0.5)
    await accha.edit("🤣")
    await asyncio.sleep(0.5)
    await accha.edit("😂")
    await asyncio.sleep(0.5)
    await accha.edit("🎉")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(

"CAACAgUAAxkBAAIDG2QhN85PjxC3IZl3hYefSbz_w60-AAI-CQAC5Nr5V3U6V4xWQpckLwQ")
    await umm.delete()
        ),
    )





