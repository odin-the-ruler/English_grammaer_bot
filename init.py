import json
# import telebot
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests



BOT_TOKEN="YOUR_BOT_TOKEN"


# with open('data.json') as f:
#     cmd_data = json.load(f)


# The URL of the JSON file
url = "https://odin-the-ruler.github.io/english_grammar/grammar.json"

# Send a GET request and get the data
response = requests.get (url)

# Parse the data as JSON
cmd_data= response.json()

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
    response = get_response(command.split()[1].lower())
    #split the message into multiple message if it has charecter more then one
    msgs = [response[i:i + 4096] for i in range(0, len(response), 4096)]
    for text in msgs:
        await update.message.reply_text(text=text)

async def help(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How to use the bot\n\n-   To use the bot, you need to type  /rules  followed by the name of the part of speech you want to learn about. For example,  /rules noun  will show you the rules for nouns.\n-   The bot will reply with a message that contains the definition, examples, and types of the part of speech you requested. It will also highlight the part of speech in the examples with bold text.\n-   You can also type  /rules all  to see a list of all the parts of speech that the bot can teach you.\n\nCommands\n_______________\n/rules partOfSpeach -> to get rules of a part of speach.\n/ping  -> to check my response time.")

async def ping(update, context):
    start = update.message.date
    end = update.message.date
    response_time = (end - start).total_seconds()
    response_time_str = f"{response_time:.2f} seconds"
    await update.message.reply_text(f"!Pong🏓\nResponse time: {response_time_str}")


async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I will help you to revise your grammar rules 😊use /help to know how to use me")


app = ApplicationBuilder().token(BOT_TOKEN).build()

# Command Handlers
cmd_handler = CommandHandler("rules", rules)
help_handler = CommandHandler("help",help)
start_handler = CommandHandler("start",start)
ping_handler = CommandHandler("ping",ping)

# Adding command Handlers
app.add_handler(cmd_handler)
app.add_handler(help_handler)
app.add_handler(start_handler)
app.add_handler(ping_handler)

app.run_polling()
