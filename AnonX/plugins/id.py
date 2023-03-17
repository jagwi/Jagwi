from AnonX import app
from pyrogram import filters


@app.on_message(filters.command('id'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"🍁𝐘𝐎𝐔𝐑 𝐈𝐃🍁: {message.from_user.id}\n{reply.from_user.first_name}'𝐒 𝐈𝐃: {reply.from_user.id}\n🥀𝐆𝐑𝐎𝐔𝐏 𝐈𝐃🥀: {message.chat.id}"
        )
    else:
        message.reply(
            f"🍁𝐘𝐎𝐔𝐑 𝐈𝐃🍁: {message.from_user.id}\n🥀𝐆𝐑𝐎𝐔𝐏 𝐈𝐃🥀: {message.chat.id}"
       )
