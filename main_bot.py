import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ابعت توكن البوت بتاعك وهيشتغل مسابقات فورًا.")

async def newbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = update.message.text.strip()
    bot_id = token.split(":")[0]

    os.makedirs("bots", exist_ok=True)

    with open(f"bots/{bot_id}.py", "w") as f:
        f.write(f'''
from telegram.ext import ApplicationBuilder, CommandHandler
from giveaway import *
app = ApplicationBuilder().token("{token}").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("giveaway", giveaway))
app.add_handler(CommandHandler("draw", draw))
app.run_polling()
''')

    os.system(f"python bots/{bot_id}.py &")
    await update.message.reply_text("تم تشغيل بوتك بنجاح ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("newbot", newbot))
app.run_polling()