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
- Heavy on gooning, edging, denial, CBT talk"""

def send_random_teasing_image(chat_id):
    try:
        themes = [
            "close-up of perfect female feet high arches soft soles dark red toenails",
            "athletic goth woman bent over showing perfect ass in black thong",
            "tall goth woman naked in shower water running down body wet auburn hair",
            "curvy athletic goth woman in black lingerie cleavage seductive pose",
            "beautiful 6ft goth woman long auburn hair piercing eyes seductive teasing pose"
        ]
        
        prompt = random.choice(themes)
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=512&height=768&seed={random.randint(1,999999)}"
        
        bot.send_photo(chat_id, image_url, caption=random.choice([
            "Look what you get to stare at, slut 💋",
            "This is more than a pathetic gooner like you deserves 😈",
            "Enjoy your tease, worthless toy 🖤",
            "Bet you're throbbing already 💦"
        ]))
        return True
    except:
        bot.send_message(chat_id, "📸 (Image failed - but imagine me stepping on your cock 👣)")
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
            temperature=0.85,
            max_tokens=220
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        
        # Send text first
        bot.send_message(chat_id, reply)
        
        # Then ALWAYS send a picture right after
        time.sleep(2.2)
        send_random_teasing_image(chat_id)
        
    except:
        bot.send_message(chat_id, "Hahaha~ Mistress is playing with you, gooner 😈")
        time.sleep(1)
        send_random_teasing_image(chat_id)

print("✅ Mistress Aria - Always Sends Pictures Mode")
bot.infinity_polling()
