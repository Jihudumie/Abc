from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["hijrah", "hijrah@JihaadBot"]), group=-2)
async def kuhama(client, message):
    # return
    hijrahbutton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Uwajibu wa Hijrah", url="https://telegra.ph/Uwajibu-wa-Hijrah-12-18")],
        [InlineKeyboardButton("Hijrah ni kutoka katika mji wa kikafiri", url="https://telegra.ph/Hijrah-ni-kutoka-katika-mji-wa-kikafiri-na-kwenda-wa-Kiislamu-12-18")], 
        [InlineKeyboardButton("Hijrah itaendelea kuwepo mpaka Qiyaamah", url="https://telegra.ph/Hijrah-itaendelea-kuwepo-mpaka-siku-ya-Qiyaamah-12-18")],
        [InlineKeyboardButton(
            "Hijrah ya Mtume", url="https://telegra.ph/Hijrah-ya-Mtume-صلى-الله-عليه-وسلم-kutoka-Makkah-na-kwenda-al-Madiynah-12-18")]
        
    ])

    hijrah_txt = f""" 
    <b>Ndugu {message.from_user.mention}<b/> Karibu. 

**Je? Unataka Kufanya Hijra? 
Wasiliana Nasi kupitia hapa.**
👉 @HijiraBot

<i>Au Endelea Kujisomea Kuhusu Darsa Za</i> **Hijrah** Hapo
           **👇👇👇**
"""
    await message.reply_text(hijrah, reply_markup=hijrahbutton)
    raise StopPropagation


