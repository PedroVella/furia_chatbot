from telegram import Update
from telegram.ext import ContextTypes

async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com as próximas partidas da FURIA
    agenda_text = (
        "*📅 Próximas partidas da FURIA:*\n\n"
        "🆚 *FURIA x G2 Esports*\n"
        "🏆 *ESL Pro League*\n"
        "📅 *04/05/2025 às 16:00*"
    )
    await update.message.reply_text(agenda_text, parse_mode="Markdown")