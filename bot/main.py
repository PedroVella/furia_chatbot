from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot.config.settings import TELEGRAM_TOKEN
from bot.handlers.elenco_handler import elenco
from bot.handlers.titulos_handler import titulos
from bot.handlers.historia_handler import historia
from bot.handlers.veterano import veterano


# Comando /start (mensagem de boas-vindas)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text = (
        "*👋 Olá, fã da FURIA CS! Como posso te ajudar?*\n\n"
        "• Use */elenco* para saber quem são os jogadores atuais da FURIA.\n"
        "• Use */titulos* para saber os principais títulos conquistados pela FURIA.\n"
        "• Use */historia* para saber mais sobre a história da FURIA.\n"
        "• Use */veterano* para saber quem é o jogador mais antigo da FURIA."
        )
    await update.message.reply_text(start_text, parse_mode="Markdown")

# Inicializando a aplicação
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Adicionando o comando /start
app.add_handler(CommandHandler("start", start))

# Adicionando o comando /elenco
app.add_handler(CommandHandler("elenco", elenco))

# Adicionando o comando /titulos
app.add_handler(CommandHandler("titulos", titulos))

# Adicionando o comando /historia
app.add_handler(CommandHandler("historia", historia))

# Adicionando o comando /veterano
app.add_handler(CommandHandler("veterano", veterano))

# Iniciando o bot com polling
app.run_polling()

