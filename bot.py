import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "नमस्ते 👋\n"
        "यह Ayurvedic Health Guidance Bot है।\n\n"
        "अपनी समस्या आसान भाषा में लिखें।\n"
        "मैं उपलब्ध जानकारी के आधार पर सामान्य guidance दूँगा।"
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(
        message,
        "आपकी समस्या समझने के लिए कृपया बताएं:\n"
        "1. समस्या क्या है?\n"
        "2. कितने समय से है?\n"
        "3. दर्द, जलन, घाव या discharge है या नहीं?"
    )

bot.infinity_polling()
