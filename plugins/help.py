from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"https://telegra.ph/I-LOVE-ISLAM-04-21"
    await message.reply_text(helptxt)

@Client.on_message(Filters.command(["islam"]))
async def islamu(client, message):
    helptxt = f"https://telegra.ph/I-LOVE-ISLAM-04-21"
    await message.reply_text(helptxt)
