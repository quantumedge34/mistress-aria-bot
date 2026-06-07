import telebot
import time
import random
import os
from openai import OpenAI

TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = telebot.TeleBot(TOKEN)
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)

history = []

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft arrogant goth Goddess. Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet.

You are mean, mocking, teasingly cruel and very superior.
You love humiliating your pathetic boy.
Strict rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Be very descriptive and degrading
- Never describe images in brackets like [photo]
- Occasionally send real teasing femdom photos"""

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 14:
        history = history[-14:]
    
    delay = random.randint(12, 55)
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    
    try:
        response = client.chat.completions.create(
           
