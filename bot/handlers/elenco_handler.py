from telegram import Update
from telegram.ext import ContextTypes

async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com o elenco atual da FURIA
    elenco_text = (
        "*🎮 Elenco atual da FURIA CS:*\n\n"
        "• 🇧🇷 *Yuurih* - Yuri Boian\n"
        "• 🇧🇷 *KSCERATO* - Kaike Cerato\n"
        "• 🇧🇷 *FalleN* - Gabriel Toledo\n"
        "• 🇰🇿 *Molodoy* - Danil Golubenko\n"
        "• 🇱🇻 *YEKINDAR* - Mareks Gaļinskis\n"
        "• 🇧🇷 *Sidde* - Sidnei Macedo (Coach)"
    )
    await update.message.reply_text(elenco_text, parse_mode="Markdown")