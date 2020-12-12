from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"https://telegra.ph/I-LOVE-ISLAM-04-21"
    await message.reply_text(helptxt)

@Client.on_message(Filters.command(["juzuu"]))
async def islamu(client, message):
    tugeme = f"kitabu \n  https://t.me/Furqanbot"
    juzuutxt = f"""https://telegra.ph/Juzuu-ya-1-Hadi-Ya-30-01-22


https://t.me/Furqanbot
"""
    await message.reply_text(juzuutxt, tugeme)
