import random
from telegram import Update
from telegram.ext import ContextTypes

giveaways = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بوت مسابقات شغال 🎉")

async def giveaway(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != "channel": return
    winners = int(context.args[0])
    cid = update.effective_chat.id
    giveaways[cid] = {"winners": winners, "users": set()}
    await context.bot.send_message(cid, f"سحب جديد – عدد الفائزين {winners}")

async def draw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cid = update.effective_chat.id
    users = list(giveaways[cid]["users"])
    wins = giveaways[cid]["winners"]
    result = random.sample(users, wins)
    await context.bot.send_message(cid, str(result))