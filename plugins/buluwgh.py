from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["buluwgh", "buluwgh@JihaadBot"]), group=-2)
async def buluwgh(client, message):
    # return
    buluwghbutton = InlineKeyboardMarkup([
        [InlineKeyboardButton("01. BULUWGH", url="https://telegra.ph/01-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-12-12-3")],
        [InlineKeyboardButton("02. BULUWGH", url="https://telegra.ph/02-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Jizya-Na-Kusitisha-Vita-07-12")], 
        [InlineKeyboardButton(
            "03. BULUWGH", url="https://telegra.ph/03-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Mashindano-Ya-Farasi-Na-Kurusha-Mishale-07-12-2")]
        
    ])

    buluwgh = f"""<b>﷽

كِتَابُ الْجِهادِ

<u>Kitabu cha Jihaad</u></b>"""
    await message.reply_text(buluwgh, reply_markup=buluwghbutton)
    raise StopPropagation
