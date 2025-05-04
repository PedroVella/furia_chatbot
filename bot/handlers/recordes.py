from telegram import Update
from telegram.ext import ContextTypes

async def recordes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com os recordes da FURIA
    recordes_text = (
        "*🏅 Recordes da FURIA no CS:GO:*\n\n"
        "• 💥 *Jogador com mais kills pela FURIA:*\n"
        "  *KSCERATO* - 12,345 kills em partidas oficiais\n\n"
        "• 🔫 *Maior número de kills em uma partida oficial:*\n"
        "  *KSCERATO* - 42 kills vs. Team Liquid – ESL Pro League 2023\n\n"
        "• ⚡ *Ace mais rápido:*\n"
        "  *yuurih* - 5 abates em 13 segundos – Mirage, 2022\n\n"
        "• 📊 *Melhor rating em um campeonato:*\n"
        "  *FalleN* - 1.35 de rating no IEM Dallas 2023\n\n"
        "• 🧠 *Jogador com mais clutches vencidos:*\n"
        "  *arT* - 97 clutches em torneios Tier 1 desde 2020"
    )
    await update.message.reply_text(recordes_text, parse_mode="Markdown")