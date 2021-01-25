
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["hijrah", "hijrah@JihaadBot"]), group=-2)
async def hama_text(client, message):
    # return
    hijrahbutton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Uwajibu wa Hijrah", url="https://telegra.ph/Uwajibu-wa-Hijrah-12-18")],
        [InlineKeyboardButton("Hijrah ni kutoka katika mji wa kikafiri", url="https://telegra.ph/Hijrah-ni-kutoka-katika-mji-wa-kikafiri-na-kwenda-wa-Kiislamu-12-18")],
        [InlineKeyboardButton("Hijrah itaendelea kuwepo mpaka Qiyaamah", url="https://telegra.ph/Hijrah-itaendelea-kuwepo-mpaka-siku-ya-Qiyaamah-12-18")],
        [InlineKeyboardButton("Hijrah ya Mtume", url="https://telegra.ph/Hijrah-ya-Mtume-صلى-الله-عليه-وسلم-kutoka-Makkah-na-kwenda-al-Madiynah-12-18")],
        [InlineKeyboardButton("Wajibu Wa Kuwa Thabiti", url="https://telegra.ph/Wajibu-Wa-Kuwa-Thabiti-01-24")],
        [InlineKeyboardButton("Fadhila Za Jihaad", url="https://telegra.ph/Fadhila-Za-Jihaad-01-24")],
        [InlineKeyboardButton("Wajibu Wa Viongozi Wa Jeshi", url="https://telegra.ph/Wajibu-Wa-Viongozi-Wa-Jeshi-01-24")],
        [InlineKeyboardButton("Al-Wahn", url="https://telegra.ph/Al-Wahn-01-24")],
        [InlineKeyboardButton("ISLAMIC STATE", url="https://telegra.ph/Ribbiyyuwna-04-26")], 
        [InlineKeyboardButton("📚 KUJITOA 👇 MUHANGA 📖", url="https://telegra.ph/KUJITOA-MUHANGA-02-21")],
        [InlineKeyboardButton("1. A'MALIYAT ISTISHAHADIYAH", url="https://telegra.ph/AMALIYAT-ISTISHAHADIYAH--KUJITOA-MUHANGA--KWA-MUJIBU-WA-QURAN--SUNNAH--NA-KAULI-MBALI-MBALI-ZA-WANACHUONI-02-21")],
        [InlineKeyboardButton(
            "2. SHARTI ZA KUJITOA MUHANGA", url="https://telegra.ph/UHALI-WA-KUJITOA-MUHANGA-KWA-MUJIBU-WA-QURAN-02-21")]
        
    ])

    hijrah = f"""

    <b>Ndugu {message.from_user.mention}<b/> Karibu. 

**Je? Unataka Kufanya Hijra? 
Wasiliana Nasi kupitia hapa.**
👉 @HijiraBot

<i>Au Endelea Kujisomea Kuhusu Darsa Za</i> **Hijrah** Hapo
           **👇👇👇**

"""
    await message.reply_text(hijrah, reply_markup=hijrahbutton)
    raise StopPropagation
