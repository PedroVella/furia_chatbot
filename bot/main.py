from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot.config.settings import TELEGRAM_TOKEN
from bot.handlers.elenco_handler import elenco
from bot.handlers.titulos_handler import titulos
from bot.handlers.historia_handler import historia
from bot.handlers.ranking_handler import ranking
from bot.handlers.redes_handler import redes
from bot.handlers.recordes import recordes
from bot.handlers.agenda_handler import agenda
from bot.handlers.comandos_handler import comandos
import os 
from bot.keep_active import start_server
start_server()


# Comando /start (mensagem de boas-vindas)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text = (
        "👋 *Olá, fã da FURIA CS! Como posso te ajudar?*\n\n"
        "📋 *Comandos disponíveis:*\n\n"
        "👥 /elenco – Ver elenco atual da FURIA\n"
        "📅 /agenda – Ver próximos jogos\n"
        "🌍 /ranking – Ver posição no ranking mundial\n"
        "🏆 /titulos – Ver títulos conquistados\n"
        "🥇 /recordes – Ver os recordes da FURIA\n"
        "📖 /historia – Conhecer a história da FURIA CS\n"
        "🔗 /redes – Redes sociais\n"
        "❓ /comandos – Mostrar todos os comandos\n"
    )
    await update.message.reply_text(start_text, parse_mode="Markdown")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Inicializando a aplicação
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Adicionando o comando /start
app.add_handler(CommandHandler("start", start))

# Adicionando o comando /elenco
app.add_handler(CommandHandler("elenco", elenco))

# Adicionando o comando /ranking
app.add_handler(CommandHandler("ranking", ranking))

# Adicionando o comando /titulos
app.add_handler(CommandHandler("titulos", titulos))

# Adicionando o comando /historia
app.add_handler(CommandHandler("historia", historia))

# Adicionando o comando /recordes
app.add_handler(CommandHandler("recordes", recordes))

# Adicionando o comando /redes
app.add_handler(CommandHandler("redes", redes))

# Adicionando o comando /agenda
app.add_handler(CommandHandler("agenda", agenda))

# Adicionando o comando /comandos
app.add_handler(CommandHandler("comandos", comandos))

# Iniciando com Webhook
if __name__ == "__main__":
    PORTA = int(os.environ.get("PORT", 8443))
    app.run_webhook(
        listen="0.0.0.0",
        port=PORTA,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"https://furia-chatbot-t5jk.onrender.com/{TELEGRAM_TOKEN}"
    )