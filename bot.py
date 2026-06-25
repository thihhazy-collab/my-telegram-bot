import os
import telebot
from flask import Flask
import google.generativeai as genai

# Flask Web Server ဆောက်ခြင်း (Render အတွက်)
app = Flask(__name__)

# တိုကင်များနှင့် API Key သတ်မှတ်ခြင်း
BOT_TOKEN = "8993816547:AAFFmltm2xLME_3iYg3VgvcNmVBxG4XG3rY"
GEMINI_API_KEY = "AQ.Ab8RN6JlXN1jGJbNF0gxhNmVmH73yRIHVQ3-C99GaPM2gz-kCA"

# AI နှင့် Bot ကို ချိတ်ဆက်ခြင်း
genai.configure(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(BOT_TOKEN)
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါဗျာ။ ကျွန်တော်ကတော့ အရာအားလုံးကို ဖြေကြားပေးနိုင်တဲ့ AI Bot ဖြစ်ပါတယ်။ သိချင်တာမှန်သမျှ လွတ်လပ်စွာ မေးမြန်းနိုင်ပါတယ်ခင်ဗျာ! 🧠✨")

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
    return "Bot is running 24/7 with Gemini AI!"

if __name__ == "__main__":
    import threading
    # Web server ကို နောက်ကွယ်ကပတ်ထားရန်
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))).start()
    print("Bot is polling...")
    bot.infinity_polling()
    
    
