import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

QUESTIONS = [
    "You only get 3 words to describe yourself – what are they?",
    "What's something everyone else loves that you secretly find overrated? How come?",
    "Would you rather have a home on the beach or in the mountains?",
    "What kind of things really makes you laugh?",
    "If you could jump into a pool full of something, what would it be?",
    "If you could be any fictional character who would it be?",
    "Have you ever had a crush on an animated character?",
    "What is the worst lie you've ever told your parents?",
    "Which habit are you proudest of breaking?",
    "If you had to pick an animal, which animal do you find the sexiest of all?",
    "Would you describe yourself as naughty or nice? Why you say so?",
    "What's your favorite joke?",
    "What's the weirdest nickname you've ever had?",
    "What would be much better if you could just change the color of it?",
    "Do you think double texting is a big deal?",
    "If your life was a movie, what would it be called?",
    "What's the last concert you went to?",
    "What do you wish you were really good at?",
    "If you were a dog, what kind of dog would you be?",
    "What's the most spontaneous thing you've ever done?",
    "If you had a time machine, would you go back in time or visit the future?",
    "What was the last show you binge-watched?",
    "If you had to rename yourself, what name would you choose?",
    "What is your favorite item of clothing?",
    "If you could be any animal, what would you be?",
]

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 *English Questions Game!*\n\n"
        "Use /roll to get a random question from the list.\n"
        "Answer it in the group and have fun! 😄",
        parse_mode="Markdown"
    )

async def roll(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 25)
    question = QUESTIONS[number - 1]
    user = update.message.from_user.first_name
    await update.message.reply_text(
        f"🎲 *{user}* rolled a *{number}*!\n\n"
        f"❓ *Question #{number}:*\n_{question}_",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roll", roll))
    print("Bot is running...")
    app.run_polling()