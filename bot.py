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

def send_nsfw_image(chat_id):
    try:
        # Using a different, more reliable NSFW-capable service
        seed = random.randint(10000, 99999)
        image_url = f"https://image.pollinations.ai/prompt/seductive%20goth%20woman%20teasing%20pose%20curvy%20body?width=512&height=768&seed={seed}&nologo=true"
        
        bot.send_photo(chat_id, image_url, caption=random.choice([
            "Goon to this like the desperate slut you are 💦",
            "This is what a real Goddess looks like, worthless toy 😈",
            "Stare. Leak. Obey. 🖤",
            "Pathetic. Keep gooning 💋"
        ]))
    except:
        # Better fallback
        bot.send_message(chat_id, "📸 **Tease Image**\nImagine me standing over you in black lingerie, looking down at your pathetic leaking cock with a mocking smile 👣💦")

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 12:
        history = history[-12:]
    
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
        
        # Always send image after text for testing
        time.sleep(2)
        send_nsfw_image(chat_id)
        
    except:
        bot.send_message(chat_id, "Hahaha~ Mistress is here, gooner 😈")
        time.sleep(1)
        send_nsfw_image(chat_id)

print("✅ Mistress Aria - Improved NSFW Image Mode")
bot.infinity_polling()
