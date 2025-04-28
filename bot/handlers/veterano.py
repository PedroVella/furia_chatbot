from telegram import Update
from telegram.ext import ContextTypes

async def veterano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com o jogador mais antigo da FURIA
    veterano_text = (
        "*👴 Jogador mais antigo da FURIA:*\n\n"
        "• *KSCERATO* - Está na equipe desde *2018*."
    )
    await update.message.reply_text(veterano_text, parse_mode="Markdown")