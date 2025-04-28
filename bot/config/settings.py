from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Acessa o token do bot do Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
