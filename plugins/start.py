from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Quran", url="https://t.me/Furqanbot")],
        [InlineKeyboardBotton("I Love Islam", url="https://telegra.ph/I-LOVE-ISLAM-04-21")],
        [InlineKeyboardButton(
            "Maktabah", url="https://t.me/Abdallaahbot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

@Client.on_message(Filters.command(["juhudi"]), group=-2)
async def juhudi(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Quran", url="https://t.me/Furqanbot")],
        [InlineKeyboardButton(
            "Viongozi", url="https://t.me/ViongiziBot")]
    ])
