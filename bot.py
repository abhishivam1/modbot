from pyrogram import Client, filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


app = Client("my_bot", api_id=1613505, api_hash='ab2ad96ee3f4900132dafe115921ba31', bot_token='6169531420:AAHKsTI9uAVoUIyPNAnoQRe04DNwR12wRyI')

@app.on_message(filters.text & ~filters.command(["start"]))
def echo(bot, message):
    bot.send_message(message.chat.id, '<b>💥 Download from @appkmods</b>')


@app.on_message(filters.command("start"))
def start(bot, message):
    bot.send_message(message.chat.id, '<b>Hi, I am a bot made by @appkmods.</b> \n\n<b>Request your mods Here!</b>')


app.run()
