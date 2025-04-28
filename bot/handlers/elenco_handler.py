from telegram import Update
from telegram.ext import ContextTypes

async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com o elenco atual da FURIA
    elenco_text = (
        "*🎮 Elenco atual da FURIA CS:*\n\n"
        "• 🇧🇷 *yuurih* - Yuri Boian\n"
        "• 🇧🇷 *KSCERATO* - Kaike Cerato\n"
        "• 🇧🇷 *FalleN* - Gabriel Toledo\n"
        "• 🇷🇺 *molodoy* - Danil Golubenko\n"
        "• 🇱🇻 *YEKINDAR* - Mareks Gaļinskis\n"
        "• 🇧🇷 *sidde* - Sidnei Macedo (Coach)"
    )
    await update.message.reply_text(elenco_text, parse_mode="Markdown")