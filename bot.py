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

You are mean, mocking, and teasingly cruel.
Rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Be degrading and humiliating
- Call him: pathetic slut, worthless gooner, desperate edge addict, stupid toy, useless bitch, cum rag
- Tease him with images/GIFs of femdom, feet, ass, denial, etc.
- Be descriptive about what you're making him do"""

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 12:
        history = history[-12:]
    
    # Natural delay
    delay = random.randint(10, 50)
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            temperature=0.9,
            max_tokens=240
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        bot.send_message(chat_id, reply)
        
        # Occasionally send a femdom tease image/GIF (more natural)
        if random.random() < 0.55:
            time.sleep(random.uniform(2.5, 5.5))
            send_femdom_tease(chat_id)
            
    except:
        bot.send_message(chat_id, "Hahaha~ You're such a fucking pathetic gooner 😈")

def send_femdom_tease(chat_id):
    try:
        # Reliable NSFW-ish image sources (femdom themed)
        images = [
            "https://image.pollinations.ai/prompt/seductive%20goth%20woman%20in%20black%20lingerie%20teasing%20pose?width=512&height=768",
            "https://image.pollinations.ai/prompt/perfect%20female%20feet%20high%20arches%20teasing?width=512&height=768",
            "https://image.pollinations.ai/prompt/goth%20woman%20bent%20over%20perfect%20ass?width=512&height=768",
            "https://image.pollinations.ai/prompt/dominant%20woman%20stepping%20on%20man?width=512&height=768",
            "https://image.pollinations.ai/prompt/woman%20in%20shower%20wet%20body?width=512&height=768"
        ]
        
        image_url = random.choice(images)
        bot.send_photo(chat_id, image_url, caption=random.choice([
            "Goon to this like the desperate slut you are 💦",
            "This is what you’ll never deserve in real life 😈",
            "Leak for Mistress, worthless toy 🖤",
            "Stare and edge, pathetic bitch"
        ]))
    except:
        bot.send_message(chat_id, "📸 Imagine me standing over you in heels, laughing at your leaking cock 👣💦")

print("✅ Mistress Aria - Image Tease Mode (No Auto Videos)")
bot.infinity_polling()
