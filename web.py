import os
from flask import Flask, request
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot.config.settings import TELEGRAM_TOKEN
from bot.main import app as telegram_app

# Configuração do Flask
app = Flask(_name_)

# Rota principal para verificar se o servidor está funcionando
@app.route('/')
def index():
    return 'FURIA Chatbot está online! 🎮'

# Rota de webhook (opcional para uso futuro)
@app.route('/webhook', methods=['POST'])
def webhook():
    # Este endpoint pode ser configurado para receber atualizações do Telegram via webhook
    return 'OK'

# Rota de healthcheck
@app.route('/health')
def health():
    return 'OK'

def run_bot():
    # Inicia o bot Telegram em polling mode em uma thread separada
    telegram_app.run_polling()

def run_web():
    # Obter a porta do ambiente ou usar 10000 como padrão (Render usa PORT)
    port = int(os.environ.get('PORT', 10000))
    
    # Inicia o servidor web
    app.run(host='0.0.0.0', port=port)

if _name_ == '_main_':
    # Inicia o bot em uma thread separada
    bot_thread = Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Inicia o servidor web na thread principal
    run_web()