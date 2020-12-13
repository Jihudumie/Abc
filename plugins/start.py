from pyrogram import Client, Filters


@Client.on_message(Filters.command(["start", "start@JihaadBot"]))
async def start(client, message):
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n Karibu ktk Majaribio"
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



