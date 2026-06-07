import os
import requests
from threading import Thread
from flask import Flask
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# Retrieve configuration from Render Environment Variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
SHRINKME_API = os.environ.get('SHRINKME_API')

# Flask setup to keep the service alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_web():
    # Render assigns a PORT dynamically; default to 10000 if not set
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    # Start the web server in a background thread
    Thread(target=run_web, daemon=True).start()
    
    # Initialize and start the Telegram bot
    print("Bot is starting...")
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # You can add your command/message handlers here
    # app_bot.add_handler(...)
    
    app_bot.run_polling()
