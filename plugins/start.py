from pyrogram import Client, Filters


@Client.on_message(Filters.command(["start", "start@JihaadBot"]))
async def start(client, message):
    welcomed = f"""<u>بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ</u>

<i>Ndugu</i>  <b><u>{message.from_user.first_name}</u></b> <i>Karibu Katika Elimu ya **Jihaad**</i>


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

Hayo  Na Mengine Allah Atakuonyesha Hapa ➠/jihaad 👈:

➠ /help 👈 Kwa Msaada zaidi..

Kwa elimu zaidi  
➠ @AbdallaahBot 👈
➠ @HamisBot 👈"""
    await message.reply_text(welcomed)

@Client.on_message(Filters.command(["help", "help@JihaadBot"]))
async def help(client, message):
    helptxt = f"""
    <b><u>{message.from_user.first_name}</u></b>
<b><i>Hapa ni sehemu ya Msaada</i></b>

🖲 <a
href='https://telegra.ph/I-LOVE-ISLAM-04-21'>I LOVE ISLAM</a>

Kama una Hitaji Kusoma Au Kusiliza Qur'an Tukufu.
❖ @Furqanbot

<u>Kwa Darsa Mbali Mbali. 
Txt 📄, Audio 🎧, Video & File N.k.</u>
❖ @Hamisbot
❖ @AbdallaahBot

Kuongea ✆ Na Mimi Au Viongozi Tuandikie ✍
Kupitia hapo ☞@ViongoziBot, Na Shidayako itafika Kwetu
Kwa Idhini ya Allah Tutakusaidia In Shaa Allah.

Allah Akujaalie Wepesi Katika Mambo yako na Akupe <b>Mwisho Mwema</b> Aamiyn

       ➠ /Jihaad 🖲
       ➠ /buluwgh  🖲"""
    await message.reply_text(helptxt)



from pyrogram import Client, Filters


@Client.on_message(Filters.command(["amulizote", "amulizote@JihawdBot"]))
async def start(client, message):
    amulizote = f"""Command Zangu Zoote Zenye Elimu Za Jihaad

All Commands
    ☟☟☟

1. /start 👈

2. /Jihaad 👈

3. /buluwgh 👈

4. /help 👈 """
    await message.reply_text(amulizote)
