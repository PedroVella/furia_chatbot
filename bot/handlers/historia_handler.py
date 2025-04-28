from telegram import Update
from telegram.ext import ContextTypes

async def historia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Respondendo com a história da FURIA
    historia_text = (
        "*📜 História da FURIA:*\n\n"
        "A *FURIA* é uma organização brasileira de esportes eletrônicos fundada em *2017* por *Jaime \"raizen\" Pádua* e *André Akkari*.\n\n"
        "• Começou em torneios brasileiros, focando em formar talentos.\n"
        "• Em *2019*, conquistou o primeiro título internacional na *DreamHack Open Rio de Janeiro*.\n"
        "• Mudou-se para os Estados Unidos, onde se destacou pelo estilo agressivo de jogo.\n"
        "• Entre *2020-2022*, foi o período de consolidação da equipe, mantendo-se entre os melhores times das Américas.\n\n"
        "Atualmente, a *FURIA* é uma das principais equipes de *CS:GO* do Brasil.\n\n"
        "_O legado da FURIA é marcado pela gestão profissional, desenvolvimento de talentos e forte presença mundial._"
    )
    await update.message.reply_text(historia_text, parse_mode="Markdown")