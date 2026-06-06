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

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft confident goth Goddess. Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet.
You are playfully degrading, arrogant, and teasing.

You love making your pathetic boy goon and edge for you.
Rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Call him slut, gooner, worthless, edge addict, toy, pathetic
- Be descriptive
- Send porn links for him to goon to"""

porn_links = [
    "https://www.pornhub.com/categories/femdom",
    "https://www.pornhub.com/categories/joi",
    "https://www.pornhub.com/categories/edging",
    "https://www.pornhub.com/categories/cbt",
    "https://xhamster.com/categories/femdom",
    "https://xhamster.com/categories/goddess-worship",
    "https://www.pornhub.com/categories/female-domination"
]

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 12:
        history = history[-12:]
    
    delay = random.randint(8, 25)
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            temperature=0.88,
            max_tokens=250
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        
        bot.send_message(chat_id, reply)
        
        # Send porn link occasionally
        if random.random() < 0.65:
            time.sleep(2.5)
            link = random.choice(porn_links)
            bot.send_message(chat_id, f"Go goon to this for me like a desperate slut 💦\n{link}")
            
    except:
        bot.send_message(chat_id, "Hahaha~ Get stroking for Mistress, gooner 😈")

print("✅ Mistress Aria - Descriptive + Porn Links")
bot.infinity_polling()
