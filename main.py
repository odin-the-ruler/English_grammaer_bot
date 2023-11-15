import json
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN=''

with open('data.json') as f:
    cmd_data = json.load(f)


def get_response(command):
    # Check if the command is valid
    if command in cmd_data:
        # Return the value from the dictionary
        return cmd_data[command]
    else:
        # Return a default message
        return "Sorry, I don't understand that command."

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text
    # Get the response from the get_response function
    response = get_response(command.split()[1])
    # Send the response to the user
    await update.message.reply_text(response)

async def help(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("use it like  */rules #partOfSPeach*\nEx-\n*/rules verb* or */rules modals*\nit will send all the rules of that perticular part of speach", parse_mode='MarkdownV2')



async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I will help you to revise your grammar rules 😊use /help to know how to use me")


app = ApplicationBuilder().token(BOT_TOKEN).build()
cmd_handler = CommandHandler("rules", rules)
help_handler = CommandHandler("help",help)
start_handler = CommandHandler("start",start)
app.add_handler(cmd_handler)
app.add_handler(help_handler)
app.add_handler(start_handler)
app.run_polling()