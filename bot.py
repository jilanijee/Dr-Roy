import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")


# =========================
# 🏠 PREMIUM HOME SCREEN
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🎵✨ *OLD HINDI MUSIC* ✨🎵\n\n"
        "👑 *Welcome to Premium Music Bot* 👑\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎶 पुराने हिंदी गानों का शानदार खजाना\n"
        "💿 1960s • 1970s • 1980s • 1990s\n"
        "🎤 Singers • 🎬 Movies • 🎼 Songs\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎧 *अपना पसंदीदा गाना खोजिए और सुनिए!*"
    )

    keyboard = [

        [
            InlineKeyboardButton("🔎 🎵 Search Song", callback_data="search_song")
        ],

        [
            InlineKeyboardButton("🎤 Search Singer", callback_data="singer"),
            InlineKeyboardButton("🎬 Search Movie", callback_data="movie"),
        ],

        [
            InlineKeyboardButton("💿 Music Library", callback_data="library"),
            InlineKeyboardButton("❤️ Favourite", callback_data="favourite"),
        ],

        [
            InlineKeyboardButton("🕰️ Recently Played", callback_data="recent"),
            InlineKeyboardButton("🔀 Random Song", callback_data="random"),
        ],

        [
            InlineKeyboardButton("👑 Premium Bot", callback_data="premium"),
        ],

        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
            InlineKeyboardButton("❓ Help", callback_data="help"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


# =========================
# 🔘 BUTTON HANDLER
# =========================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "search_song":

        await query.message.reply_text(
            "🔎🎵 *SEARCH SONG*\n\n"
            "अपना गाना इस तरह लिखें:\n\n"
            "👉 `Lag Ja Gale`\n"
            "👉 `Pal Pal Dil Ke Paas`\n"
            "👉 `Ajeeb Dastan Hai Yeh`\n\n"
            "🎧 फिर मैं आपके लिए search करूँगा।",
            parse_mode="Markdown"
        )

    elif query.data == "singer":

        await query.message.reply_text(
            "🎤✨ *SEARCH SINGER*\n\n"
            "Singer का नाम लिखें।\n\n"
            "उदाहरण:\n"
            "🎙️ Kishore Kumar\n"
            "🎙️ Lata Mangeshkar\n"
            "🎙️ Mohammed Rafi\n"
            "🎙️ Asha Bhosle"
        )

    elif query.data == "movie":

        await query.message.reply_text(
            "🎬✨ *SEARCH MOVIE*\n\n"
            "Movie का नाम लिखें और उसके पुराने गाने खोजें।"
        )

    elif query.data == "library":

        await query.message.reply_text(
            "💿🎵 *MUSIC LIBRARY*\n\n"
            "🎶 1960s\n"
            "🎶 1970s\n"
            "🎶 1980s\n"
            "🎶 1990s\n\n"
            "✨ Music Library जल्द तैयार होगी।"
        )

    elif query.data == "favourite":

        await query.message.reply_text(
            "❤️ *YOUR FAVOURITE SONGS*\n\n"
            "आपके पसंदीदा गाने यहाँ दिखाई देंगे।"
        )

    elif query.data == "recent":

        await query.message.reply_text(
            "🕰️ *RECENTLY PLAYED*\n\n"
            "आपके हाल में सुने गए गाने यहाँ दिखाई देंगे।"
        )

    elif query.data == "random":

        await query.message.reply_text(
            "🔀🎵 *RANDOM SONG*\n\n"
            "आपके लिए एक random old Hindi song चुना जाएगा।"
        )

    elif query.data == "premium":

        await query.message.reply_text(
            "👑✨ *PREMIUM MUSIC EXPERIENCE* ✨👑\n\n"
            "🎵 Old Hindi Songs\n"
            "🎤 Singer Search\n"
            "🎬 Movie Search\n"
            "💿 Music Library\n"
            "❤️ Favourite Songs\n"
            "🔀 Random Songs\n"
            "🎨 Premium Background\n"
            "🎞️ Animated GIF Elements\n\n"
            "🔥 बहुत जल्द और भी premium features!"
        )

    elif query.data == "about":

        await query.message.reply_text(
            "ℹ️ *ABOUT OLD HINDI MUSIC BOT*\n\n"
            "🎶 पुराने हिंदी संगीत के लिए बनाया गया\n"
            "एक premium Telegram music experience.\n\n"
            "💿 Old is Gold ❤️"
        )

    elif query.data == "help":

        await query.message.reply_text(
            "❓ *HELP*\n\n"
            "🔎 Search Song — गाना खोजें\n"
            "🎤 Search Singer — Singer के गाने खोजें\n"
            "🎬 Search Movie — Movie के गाने खोजें\n"
            "❤️ Favourite — पसंदीदा गाने\n"
            "🔀 Random — Random song"
        )


# =========================
# 🚀 BOT START
# =========================
def main():

    if not TOKEN:
        raise ValueError("BOT_TOKEN नहीं मिला!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🎵 Old Hindi Music Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
