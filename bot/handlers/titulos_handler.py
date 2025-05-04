from telegram import Update
from telegram.ext import ContextTypes

async def titulos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com os principais títulos da FURIA
    titulos_text = (
        "*🏆 Principais títulos conquistados pela FURIA no CS:GO:*\n\n"
        "1. *EMF CS:GO World Invitational 2019*\n"
        "2. *Arctic Invitational 2019*\n"
        "3. *DreamHack Masters Spring 2020: North America*\n"
        "4. *ESL Pro League Season 12: North America*\n"
        "5. *IEM New York 2020: North America*\n"
        "6. *Gamers Without Borders 2021: North America*\n"
        "7. *Elisa Invitational Fall 2021*\n"
        "8. *ESL Challenger February 2022*\n"
        "9. *ESL Challenger Melbourne 2022*\n"
        "10. *Elisa Masters Espoo 2022*"
    )
    await update.message.reply_text(titulos_text, parse_mode="Markdown")