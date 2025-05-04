from telegram import Update
from telegram.ext import ContextTypes

async def redes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com as redes sociais oficiais da FURIA
    redes_text = (
        "*🌐 Redes Sociais Oficiais da FURIA:*\n\n"
        "• 🐦 *Twitter:* [@FURIA](https://twitter.com/FURIA)\n"
        "• 📸 *Instagram:* [@furiagg](https://instagram.com/furiagg)\n"
        "• ▶️ *YouTube:* [FURIA CS](https://www.youtube.com/@FURIAggCS/featured)"
    )
    await update.message.reply_text(redes_text, parse_mode="Markdown")