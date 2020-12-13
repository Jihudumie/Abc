from pyrogram import Client, Filters


@Client.on_message(Filters.command(["start", "start@JihaadBot"]))
async def start(client, message):
    welcomed = f"""<u>بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ</u>

<i>Ndugu</i> <b>{message.from_user.first_name}</b> <i>Karibu Kwa Ajili ya Allaah</i>


       ➠ /Jihaad 🖲
       ➠ /buluwgh  🖲
<b>JIHAAD</b> imekusanya kila aina ya ibada za kiroho na kiwiliwili, kuikinai dunia, kuihama nchi na kuyahama matamanio na hii ndiyo maana ikapewa jina la ‘Uchaji Allaah’, kwani imekuja katika Hadiyth kuwa:

<b>‘Uchaji __Allaah wa umma wangu ni Jihaad__ katika njia ya Allaah.”</b>

Na ndani yake mna kuitakasa nafsi, kuitakasa mali, na kumuuzia Allaah nafsi, na haya yote ni matunda ya mapenzi na imani na yakini na kuelekea kwa Allaah (Subhaanahu wa Ta’ala).

NDUGU ZANGU KATIKA IMAAN, MIMI NDUGU YENU NIMETENGENEZEA ROBOT HII 👉 @JihaadBot. ILI TUPATE KUJIFUNZA KWA WEPESI NA KWA WAKATI WOWOTE.

__Gusa hapa__ ➠ /Jihaad
__Au hapo__ ➠/buluwgh

 Kupata Vitabu 📚 Au darsa 📖

Mtume wa Allaah (Swalla Allaahu ‘alayhi wa sallam) amesema:
<b>“Shahidi hahisi maumivu ya kuuliwa ila kama mmoja wenu anavyohisi maumivu ya kufinywa.”</b>

Hayo  Na Mengine Allah Atakuonyesha Hapa ➠/jihaad:

➠ /help Kwa Msaada zaidi..

Kwa elimu zaidi  
➠ @AbdallaahBot
➠ @HamisBot"""
    await message.reply_text(welcomed)

@Client.on_message(Filters.command(["help", "help@JihaadBot"]))
async def help(client, message):
    helptxt = f"""<b>Hapa ni sehemu ya Msaada</b>

🖲 <a
href='https://telegra.ph/I-LOVE-ISLAM-04-21'>I LOVE ISLAM</a>

Kama una Hitaji Kusoma Au Kusiliza Qur'an Tukufu.
❖ @Furqanbot

<u>Kwa Darsa Mbali Mbali. 
Txt 📄, Audio 🎧, Video & File N.k.</u>
❖ @Hamisbot / ❖ @AbdallaahBot

Kuongea Nasi Au Viongozi Tuandikie ✍.
👉 @ViongoziBot Na Shidayako itafika Kwetu
Kwa Idhini ya Allah Tutakusaidia In Shaa Allah.

Allah Akujaalie Wepesi Katika Mambo yako na Akupe <b>Mwisho Mwema</b> Aamiyn"""
    await message.reply_text(helptxt)



