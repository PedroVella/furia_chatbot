from telegram import Update
from telegram.ext import ContextTypes

async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "📋 *Comandos disponíveis:*\n\n"
        "👥 /elenco – Ver elenco atual da FURIA\n"
         "📅 /agenda – Ver próximos jogos\n"
         "🌍 /ranking – Ver posição no ranking mundial\n"
        "🏆 /titulos – Ver títulos conquistados\n"
        "🥇 /recordes – Ver os recordes da Furia\n"
        "📖 /historia – Conhecer a história da FURIA CS\n"
        "🔗 /contato – Contato e redes sociais\n"
        "❓ /comandos – Mostrar todos os comandos\n"
    )

    await update.message.reply_text(texto, parse_mode="Markdown")
