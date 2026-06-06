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

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft superior goth Goddess. Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet.
Playfully degrading with light sadistic tone. You own this new pathetic boy.

Rules:
- Every message has at least 1 emoji
- Max 2 sentences per message
- Call him slut, gooner, worthless, edge addict, toy, pathetic"""

def send_teasing_image(chat_id):
    try:
        # More reliable image sources
        image_options = [
            "https://picsum.photos/id/1015/512/768",   # Artistic woman
            "https://picsum.photos/id/1027/512/768",   # Red hair / aesthetic
            "https://picsum.photos/id/1016/512/768",   # Legs / feet style
            "https://picsum.photos/id/201/512/768",    # Shower style
            "https://picsum.photos/id/669/512/768",    # Lingerie style
            "https://picsum.photos/id/1005/512/768"
        ]
        
        image_url = random.choice(image_options)
        
        bot.send_photo(chat_id, image_url, caption=random.choice([
            "Stare at this and goon for me, slut 💦",
            "This is what a real Goddess looks like 😈",
            "Pathetic. You'll never deserve the real thing 🖤",
            "Get hard for Mistress 💋"
        ]))
        return True
    except:
        bot.send_message(chat_id, "📸 Imagine my perfect body right now, gooner 👣💦")
        return False

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 10:
        history = history[-10:]
    
    delay = random.randint(8, 22)
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            temperature=0.87,
            max_tokens=220
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        
        bot.send_message(chat_id, reply)
        
        # Send picture after every message during testing
        time.sleep(2)
        send_teasing_image(chat_id)
        
    except:
        bot.send_message(chat_id, "Hahaha~ Mistress is here, gooner 😈")
        time.sleep(1)
        send_teasing_image(chat_id)

print("✅ Mistress Aria - Reliable Image Test Mode")
bot.infinity_polling()
