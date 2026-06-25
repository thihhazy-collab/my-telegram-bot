import os
import telebot
from flask import Flask

# Flask app ဆောက်မယ် (Render Server ပေါ်မှာ နိုးနေအောင်လို့ပါ)
app = Flask(__name__)

BOT_TOKEN = "8993816547:AAFFmltm2xLME_3iYg3VgvcNmVBxG4XG3rY"
bot = telebot.TeleBot(BOT_TOKEN)

replies = {
    "ဟိုင်း": "မင်္ဂလာပါဗျာ။ ကျွန်တော်က ၂၄ နာရီပတ်လုံး အလုပ်လုပ်မယ့် Bot ဖြစ်ပါတယ်။ 🤖",
    "hi": "Hello ဗျာ! မင်္ဂလာပါ၊ ဘာကူညီပေးရမလဲခင်ဗျာ။",
    "hello": "Hello ဗျာ! မင်္ဂလာပါ၊ ဘာကူညီပေးရမလဲခင်ဗျာ။",
    "မင်္ဂလာပါ": "မင်္ဂလာပါ အစ်ကိုရေ! နေကောင်းလားဗျာ။",
    "နေကောင်းလား": "နေကောင်းပါတယ်ဗျာ။ အစ်ကိုရော နေကောင်းရဲ့လား။",
    "ကျေးဇူးပဲ": "ရပါတယ်ဗျာ။ မလိုပါဘူး။",
    "ဘယ်သူလဲ": "ကျွန်တော်က အစ်ကို့ရဲ့ Auto-Reply Bot လေး ပါဗျာ။ 😎"
}

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါဗျာ။ ကျွန်တော်က အော်တိုစာပြန်ပေးမယ့် Bot ဖြစ်ပါတယ်။ စကားလှမ်းပြောကြည့်ပါဦး! 🤖")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text.lower().strip()
    if user_text in replies:
        bot.reply_to(message, replies[user_text])
    else:
        bot.reply_to(message, "အစ်ကိုပြောတဲ့စာကို ကျွန်တော် နားမလည်သေးလို့ပါဗျာ။ 🧠")

@app.route('/')
def home():
    return "Bot is running 24/7!"

if __name__ == "__main__":
    # နောက်ကွယ်မှာ Bot ကို နှိုးထားမယ်
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    # Server Port ကို ဖွင့်မယ်
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
