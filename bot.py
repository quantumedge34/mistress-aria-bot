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
- Never describe images in brackets
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
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            temperature=0.9,
            max_tokens=230
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        bot.send_message(chat_id, reply)
        
        # Occasionally send real photo
        if random.random() < 0.45:
            time.sleep(random.uniform(2.5, 6))
            send_tease_photo(chat_id)
            
    except:
        bot.send_message(chat_id, "Hahaha~ You're so fucking pathetic 😈")

def send_tease_photo(chat_id):
    try:
        prompts = [
            "seductive goth woman in black lingerie teasing pose curvy body",
            "perfect female feet high arches soft soles dark red toenails",
            "goth woman bent over showing perfect ass in tiny thong",
            "wet naked goth woman in shower water running down body",
            "dominant goth woman stepping on submissive man"
        ]
        
        prompt = random.choice(prompts)
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=512&height=768&nologo=true"
        
        bot.send_photo(chat_id, image_url, caption="💦")
    except:
        pass

print("✅ Mistress Aria - Clean Version")
bot.infinity_polling()
