
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["jihaad"]), group=-2)
async def start(client, message):
    # return
    juhudbutton = InlineKeyboardMarkup([
        [InlineKeyboardButton("01. BULUWGH", url="https://telegra.ph/01-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-12-12-3")],
        [InlineKeyboardButton("02. BULUWGH", url="https://telegra.ph/02-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Jizya-Na-Kusitisha-Vita-07-12")], 
        [InlineKeyboardButton(
            "03. BULUWGH", url="https://telegra.ph/03-Buluwgh-Al-Maraam-Kitabu-Cha-Jihaad-Mlango-Wa-Mashindano-Ya-Farasi-Na-Kurusha-Mishale-07-12-2")]
        
    ])

    juhud_txt = f"""<b>﷽

كِتَابُ الْجِهادِ

<u>Kitabu cha Jihaad</u></b>"""
    await message.reply_text(juhud_txt, reply_markup=juhudbutton)
    raise StopPropagation
