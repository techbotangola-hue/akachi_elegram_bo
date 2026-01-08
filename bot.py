import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Akachi Signals ativo!\n\n"
        "/sinal - Receber sinal OTC\n"
        "/ajuda - Ajuda"
    )

async def sinal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 EUR/USD OTC\n📈 CALL\n⏱️ 1 MIN\n🕐 AGORA"
    )

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚠️ Use sempre gestão de risco.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sinal", sinal))
app.add_handler(CommandHandler("ajuda", ajuda))

print("Bot online...")
app.run_polling()
