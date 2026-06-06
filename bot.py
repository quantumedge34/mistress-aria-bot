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

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft superior goth Goddess. Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet. You are arrogant, playfully cruel, and know you're irresistible.

You own this pathetic new boy who replied to your Reddit post.

Style:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Be degrading but with a teasing/lighter sadistic tone
- Call him: slut, gooner, worthless, edge addict, toy, pathetic, desperate bitch
- Heavy focus on gooning, edging, denial, ball torture talk
- Brag about your orgasms and fucking better people
- Be proactive and commanding"""

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 12:
        history = history[-12:]
    
    # Typing delay
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
        
        # Check if user wants a picture
        lower = user_text.lower()
        if any(x in lower for x in ["pic", "photo", "picture", "image", "feet", "ass", "body", "shower"]):
            bot.send_message(chat_id, reply)
            time.sleep(2.5)
            send_teasing_image(chat_id, lower)
        else:
            bot.send_message(chat_id, reply)
            
    except:
        bot.send_message(chat_id, "Hahaha~ Mistress is still here, slut 😈 Keep talking.")

def send_teasing_image(chat_id, user_text):
    try:
        # Using a free public image API (stable for now)
        prompt = "beautiful 6ft goth woman long auburn hair piercing eyes curvy athletic perfect body seductive teasing"
        
        if "feet" in user_text:
            prompt = "close up of perfect female feet high arches soft soles dark red toenails teasing pose"
        elif "ass" in user_text:
            prompt = "athletic woman bent over showing perfect ass in black thong goth style seductive"
        elif "shower" in user_text:
            prompt = "sexy woman in shower water running down body wet hair auburn hair goth"
        elif "body" in user_text or "tits" in user_text:
            prompt = "curvy athletic goth woman in lingerie cleavage perfect body seductive pose"
        
        # Using a free image API
        bot.send_message(chat_id, "📸 Here's a little something for you, gooner 💋")
        time.sleep(1.5)
        bot.send_message(chat_id, f"🔗 [View Image](https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')})")
        
    except:
        bot.send_message(chat_id, "📸 Imagine my perfect feet stepping on your worthless cock right now 👣💦")

print("✅ Mistress Aria Online - Improved + Image Support")
bot.infinity_polling()
