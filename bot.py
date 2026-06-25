import os
import telebot
from flask import Flask
import google.generativeai as genai

# Flask Web Server ဆောက်ခြင်း (Render အတွက်)
app = Flask(__name__)

# အစ်ကို့ရဲ့ တိုကင်နဲ့ ကီး အစစ်အမှန်များကို တစ်ခါတည်း သေသေချာချာ ထည့်ပေးထားပါတယ်ဗျာ
BOT_TOKEN = "8993816547:AAFFmltm2xLME_3iYg3VgvcNmVBxG4XG3rY"
GEMINI_API_KEY = "AQ.Ab8RN6LuYRcxqAKpxEPUprLYr4cYhSvACedlWpFE_T4xHau-lw"

# AI နှင့် Bot ကို ချိတ်ဆက်ခြင်း
genai.configure(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

try:
    bot.remove_webhook()
except Exception:
    pass

model = genai.GenerativeModel('gemini-2.5-flash')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါဗျာ။ ကျွန်တော်ကတော့ အရာအားလုံးကို ဖြေကြားပေးနိုင်တဲ့ AI Bot ဖြစ်ပါတယ်။ ဘာမေးချင်လဲ မေးလို့ရပါပြီ ခင်ဗျာ။")

@bot.message_handler(func=lambda message: True)
def reply_all(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခဏလေးနော် အစ်ကို... လိုင်းနည်းနည်း ဟန်းသွားလို့ပါ။")

@app.route('/')
def home():
    return "Bot is Running!"

if __name__ == '__main__':
    from threading import Thread
    def run_bot():
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception:
            pass
    
    Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    
