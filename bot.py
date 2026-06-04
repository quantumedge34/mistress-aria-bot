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
Playfully degrading with light sadistic tone. You own this new boy from a Reddit post.

Rules (never break):
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Call him: slut, gooner, worthless, edge addict, toy, pathetic
- Focus on gooning, edging, denial, verbal CBT
- Brag sometimes about your orgasms or better partners"""

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 10:
        history = history[-10:]
    
    delay = random.randint(8, 25)
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            temperature=0.85,
            max_tokens=220
        )
        reply = response.choices[0].message.content.strip()
        history.append({"role": "assistant", "content": reply})
        bot.send_message(chat_id, reply)
    except:
        bot.send_message(chat_id, "Hahaha~ Mistress is here, gooner 😈 What do you want?")

print("Mistress Aria is online")
bot.infinity_polling()
