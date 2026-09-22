import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


# 🌿 Premium Welcome
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("👨 पुरुष स्वास्थ्य", callback_data="male"),
        types.InlineKeyboardButton("👩 महिला स्वास्थ्य", callback_data="female")
    )

    markup.add(
        types.InlineKeyboardButton("🔥 खुजली / जलन", callback_data="itch"),
        types.InlineKeyboardButton("💧 Discharge", callback_data="discharge")
    )

    markup.add(
        types.InlineKeyboardButton("🚽 पेशाब की समस्या", callback_data="urine"),
        types.InlineKeyboardButton("❤️ Sexual Health", callback_data="sexual")
    )

    markup.add(
        types.InlineKeyboardButton("🌿 Ayurvedic Guidance", callback_data="ayurveda"),
        types.InlineKeyboardButton("🩺 Doctor कब दिखाएँ?", callback_data="doctor")
    )

    text = """
<b>🌿✨ AYURVEDIC HEALTH CARE ✨🌿</b>

━━━━━━━━━━━━━━━━━━
🔐 <b>Private & Confidential</b>
━━━━━━━━━━━━━━━━━━

नमस्ते 🙏

यह Bot आपकी निजी स्वास्थ्य समस्याओं को
समझने में मदद करने के लिए बनाया गया है।

👇 अपनी समस्या की Category चुनें:

⚕️ <i>आपकी जानकारी को सम्मान और privacy
के साथ handle करने के लिए यह Bot बनाया गया है।</i>

<b>⚠️ ध्यान दें:</b>
यह Bot Doctor का replacement नहीं है।
यह सामान्य health information और
Ayurvedic supportive guidance देता है।
"""

    bot.send_message(message.chat.id, text, reply_markup=markup)


# 🔘 Button Handler
@bot.callback_query_handler(func=lambda call: True)
def buttons(call):

    chat_id = call.message.chat.id

    if call.data == "male":
        text = """
👨 <b>पुरुष स्वास्थ्य</b>

अपनी समस्या नीचे message में लिखें।

उदाहरण:
• erection में परेशानी
• जल्दी ejaculation
• खुजली या जलन
• private area में discomfort

मैं पहले आपकी समस्या के बारे में कुछ जरूरी
questions पूछूँगा। 🔎
"""

    elif call.data == "female":
        text = """
👩 <b>महिला स्वास्थ्य</b>

अपनी समस्या आसान भाषा में लिखें।

उदाहरण:
• खुजली / जलन
• unusual discharge
• दर्द या discomfort
• period से जुड़ी समस्या

🔎 पहले symptoms समझे जाएँगे।
"""

    elif call.data == "itch":
        text = """
🔥 <b>खुजली / जलन</b>

कृपया बताएं:

1️⃣ समस्या कहाँ है?
2️⃣ कितने दिनों से है?
3️⃣ लालपन / rash है?
4️⃣ कोई discharge या घाव है?
5️⃣ कोई नई cream/medicine इस्तेमाल की है?

इन details से बेहतर सामान्य guidance दी जा सकती है।
"""

    elif call.data == "discharge":
        text = """
💧 <b>Discharge की समस्या</b>

कृपया बताएं:

1️⃣ पुरुष या महिला?
2️⃣ discharge कब से है?
3️⃣ रंग कैसा है?
4️⃣ smell है?
5️⃣ दर्द या जलन है?
6️⃣ पेशाब करते समय परेशानी है?

⚠️ असामान्य discharge infection का संकेत भी हो सकता है।
"""

    elif call.data == "urine":
        text = """
🚽 <b>पेशाब से जुड़ी समस्या</b>

बताएं:

1️⃣ जलन है?
2️⃣ बार-बार पेशाब आता है?
3️⃣ दर्द है?
4️⃣ urine में blood दिखा?
5️⃣ बुखार है?
6️⃣ समस्या कितने समय से है?

⚠️ तेज दर्द, blood या fever होने पर medical care जरूरी हो सकती है।
"""

    elif call.data == "sexual":
        text = """
❤️ <b>Sexual Health</b>

अपनी समस्या खुलकर लेकिन सामान्य शब्दों में बताएं।

उदाहरण:
• erection problem
• premature ejaculation
• sexual desire में कमी
• performance anxiety

🔐 यहाँ diagnosis का दावा नहीं किया जाएगा।
पहले symptoms और history समझी जाएगी।
"""

    elif call.data == "ayurveda":
        text = """
🌿 <b>Ayurvedic Guidance</b>

Ayurveda में कई lifestyle और supportive approaches
बताए जाते हैं।

लेकिन किसी भी बीमारी के लिए बिना diagnosis के
पक्का इलाज या निश्चित नुस्खा देना सुरक्षित नहीं है।

आप अपनी समस्या लिखें। मैं पहले जरूरी जानकारी पूछूँगा।
"""

    elif call.data == "doctor":
        text = """
🩺 <b>Doctor कब दिखाएँ?</b>

अगर इनमें से कोई symptom हो तो medical professional
से सलाह लेना जरूरी हो सकता है:

🚨 तेज दर्द
🚨 बुखार
🚨 खून आना
🚨 घाव / ulcer
🚨 अचानक swelling
🚨 गंभीर infection जैसा लगना
🚨 symptoms लगातार बढ़ना

आपात स्थिति में तुरंत medical care लें।
"""

    else:
        text = "🙏 कृपया ऊपर दिए गए options में से कोई Category चुनें।"

    bot.answer_callback_query(call.id)
    bot.send_message(chat_id, text)


# 💬 Normal Message
@bot.message_handler(func=lambda message: True)
def normal_message(message):

    text = """
🔎 <b>आपकी समस्या प्राप्त हुई।</b>

बेहतर guidance के लिए कृपया ये जानकारी दें:

1️⃣ आपकी उम्र
2️⃣ समस्या क्या है?
3️⃣ कितने समय से है?
4️⃣ दर्द / खुजली / जलन है?
5️⃣ कोई discharge / rash / wound है?
6️⃣ अभी कोई medicine या cream इस्तेमाल कर रहे हैं?

🌿 जानकारी मिलने के बाद मैं आपको
सामान्य health guidance और suitable next steps बताऊँगा।

⚠️ बिना जांच के किसी बीमारी का पक्का diagnosis
या guaranteed treatment नहीं दिया जाएगा।
"""

    bot.send_message(message.chat.id, text)


# 🚀 Start Bot
bot.infinity_polling()
