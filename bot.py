import os
import telebot
from flask import Flask
import google.generativeai as genai

# Flask Web Server ဆောက်ခြင်း (Render အတွက်)
app = Flask(__name__)

# တိုကင်များနှင့် API Key သတ်မှတ်ခြင်း
BOT_TOKEN = "8993816547:AAFFmltm2xL4Xm_8Z-Yp9K9K9K6vRE6mZxs"
GEMINI_API_KEY = "AQ.Ab8RN6KmLbKjrWozzx1wP_EXAMPLE_KEY" # <--- အစ်ကို့ရဲ့ API Key အမှန်ကြီးကို ဒီနေရာမှာ ပြန်ထည့်ပေးပါနော်

# AI နှင့် Bot ကို ချိတ်ဆက်ခြင်း
genai.configure(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()
model = genai.GenerativeModel('gemini-2.5-flash')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါဗျာ။ ကျွန်တော်ကတော့ အရာအားလုံးကို ဖြေကြားပေးနိုင်တဲ့ AI Bot ဖြစ်ပါတယ်။ သီချင်းလည်း တောင်းလို့ရပါတယ် ခင်ဗျာ။")

@bot.message_handler(func=lambda message: True)
def reply_all(message):
    try:
        # လူက မေးလိုက်တဲ့စာကို AI ဆီ ပို့ပြီး အဖြေတောင်းခြင်း
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခဏလေးနော် အစ်ကို... လိုင်းနည်းနည်း ဟန်းသွားလို့ပါ။")

@app.route('/')
def home():
    return "Bot is Running!"

if __name__ == '__main__':
    # Render အတွက် Web Server ရော Bot ရော တွဲပတ်ခြင်း
    from threading import Thread
    def run_bot():
        bot.infinity_polling()
    
    Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    
