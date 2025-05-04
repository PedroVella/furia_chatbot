from telegram import Update
from telegram.ext import ContextTypes

async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com o ranking atual da FURIA
    ranking_text = (
        "*🌍 Ranking Atual da FURIA no Cenário Mundial:*\n\n"
        "🔝 *Posição:* 17º lugar\n"
        "📊 *Fonte:* HLTV.org\n\n"
        "🔥 A FURIA continua representando o Brasil no topo do CS:GO mundial!"
    )
    await update.message.reply_text(ranking_text, parse_mode="Markdown")