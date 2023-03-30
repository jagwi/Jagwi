from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils import bot_sys_stats
from AnonX.utils.decorators.language import language
from AnonX.utils.inline.play import close_keyboard

### Commands
ping = get_command("PING_COMMAND")

@app.on_message(filters.command("ping"))
async def restart(client, ma: Message):
    await ma.delete()
    accha = await ma.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await ma.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(2)
    await ma.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )

    start = datetime.now()
    pytgping = await Anon.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=close_keyboard
    )
