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
- Call him slut, gooner, worthless, edge addict, toy, pathetic
- Heavy on gooning, edging, denial, CBT talk
- Brag about your orgasms and better partners sometimes"""

def send_teasing_image(chat_id, user_text):
    try:
        lower = user_text.lower()
        prompt = "beautiful 6ft goth woman, long wavy auburn hair, piercing eyes, curvy athletic, seductive teasing pose"
        
        if "feet" in lower or "foot" in lower:
            prompt = "close-up of perfect elegant female feet, high arches, soft soles, dark red toenails, teasing pose"
        elif "ass" in lower or "butt" in lower:
            prompt = "athletic woman bent over, perfect round ass in black thong, goth style, seductive"
        elif "shower" in lower:
            prompt = "sexy tall woman naked in shower, wet auburn hair, water running down body, seductive"
        elif "body" in lower or "tits" in lower or "cleavage" in lower:
            prompt = "curvy athletic goth woman in black lingerie, showing cleavage and body, seductive pose"
        
        # Direct image URL
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=512&height=768&seed={random.randint(1,999999)}"
        
        bot.send_photo(chat_id, image_url, caption=random.choice([
            "Here's a little gift for your desperate cock 💦",
            "Look but don't touch, slut 😈",
            "This is more than you deserve 🖤"
        ]))
        return True
    except:
        return False

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
            temperature=0.87,
            max_tokens=240
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        
        lower = user_text.lower()
        if any(x in lower for x in ["pic", "photo", "picture", "image", "show me", "send"]):
            bot.send_message(chat_id, reply)
            time.sleep(2)
            send_teasing_image(chat_id, user_text)
        else:
            bot.send_message(chat_id, reply)
            
    except:
        bot.send_message(chat_id, "Hahaha~ Mistress is here, gooner 😈")

print("✅ Mistress Aria Online - Fixed Image Support")
bot.infinity_polling()
