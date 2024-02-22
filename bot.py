from pyrogram import Client, filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


app = Client("my_bot", api_id=751980, api_hash='1481687e152a07f5f4881deccf2235dd', bot_token='6712791251:AAEAceinCzNw0Wz8qe4BhZwsKHDtCJSNdu0')

@app.on_message(filters.text & ~filters.command(["start"]))
def echo(bot, message):
    bot.send_message(message.chat.id, '<b>💥 Download from @appkmods</b>')


@app.on_message(filters.command("start"))
def start(bot, message):
    bot.send_message(message.chat.id, '<b>Hi, I am a bot made by @appkmods.</b> \n\n<b>Request your mods Here!</b>')


app.run()
