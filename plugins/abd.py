from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["hamis"]), group=-2)
async def start(client, message):
    # return
    gehabutton = InlineKeyboardMarkup([
        [InlineKeyboardButton("KITABU", url="https://t.me/Furqanbot")],
        [InlineKeyboardButton("ISRAA", url="https://telegra.ph/017---Al-Israa-12-29")], 
        [InlineKeyboardButton(
            "NYUMBANI", url="https://t.me/Abdallaahbot")]
        
    ])

    abdallaah = f"Hey <b>{message.from_user.first_name}</b>\n/Master Karibu Saaana"
    await message.reply_text(abdallaah, reply_markup=gehabutton)
    raise StopPropagation
