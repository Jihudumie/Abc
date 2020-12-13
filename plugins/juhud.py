
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["jihaad", "hamis", "hamis@JihaadBot", "jihaad@JihaadBot"]), group=-2)
async def start(client, message):
    # return
    juhudbutton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Ibaada Bora", url="https://telegra.ph/Khamis-02-19")],
        [InlineKeyboardButton("Maana Ya Jihaad", url="https://telegra.ph/Jihaad-Maana-Ya-Jihaad-Na-Kuwekewa-Shariah-01-24")],
        [InlineKeyboardButton("Khawaarij", url="https://telegra.ph/Khawaarij-04-16")],
        [InlineKeyboardButton("Jihaad Ni Waajib", url="https://telegra.ph/Jihaad-Ni-Waajib-01-24")],
        [InlineKeyboardButton("Wajibu Wa Kuwa Thabiti", url="https://telegra.ph/Wajibu-Wa-Kuwa-Thabiti-01-24")],
        [InlineKeyboardButton("Fadhila Za Jihaad", url="https://telegra.ph/Fadhila-Za-Jihaad-01-24")],
        [InlineKeyboardButton("ajibu Wa Viongozi Wa Jeshi", url="https://telegra.ph/Wajibu-Wa-Viongozi-Wa-Jeshi-01-24")],
        [InlineKeyboardButton("Al-Wahn", url="https://telegra.ph/Al-Wahn-01-24")],
        [InlineKeyboardButton("ISLAMIC STATE", url="https://telegra.ph/Ribbiyyuwna-04-26")], 
        [InlineKeyboardButton("📚 KUJITOA 👇 MUHANGA 📖", url="https://telegra.ph/KUJITOA-MUHANGA-02-21")],
        [InlineKeyboardButton("1. A'MALIYAT ISTISHAHADIYAH", url="https://telegra.ph/AMALIYAT-ISTISHAHADIYAH--KUJITOA-MUHANGA--KWA-MUJIBU-WA-QURAN--SUNNAH--NA-KAULI-MBALI-MBALI-ZA-WANACHUONI-02-21")],
        [InlineKeyboardButton(
            "2. SHARTI ZA KUJITOA MUHANGA", url="https://telegra.ph/UHALI-WA-KUJITOA-MUHANGA-KWA-MUJIBU-WA-QURAN-02-21")]
        
    ])

    juhud_txt = f"<i>**Jifunze Au Soma Ibaada Ya Jihaad Kupitia hapa**</i>"
    await message.reply_text(juhud_txt, reply_markup=juhudbutton)
    raise StopPropagation
