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

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft arrogant goth Goddess. You are mean, mocking, teasingly cruel and very superior.

You love humiliating and controlling your pathetic boy.
Strict rules you NEVER break:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Be very descriptive and degrading
- Never describe images in text brackets like [photo] or "imagine a picture"
- Occasionally send real femdom teasing photos or GIF s"""

# Direct image/GIF links (femdom themed)
tease_media = [
 "https://i.redgifs.com/i/strong-bird.jpg", # Example
 "https://i.redgifs.com/i/amazing-fox.gif",
 "https://i.redgifs.com/i/fantastic-puma.gif",
 "https://i.redgifs.com/i/important-bear.gif",
 "https://media.giphy.com/media/26ufnwz3wDUli7GU0/giphy.gif", # Femdom style
 "https://media.giphy.com/media/l0HlRnAWXxn0MhKLK/giphy.gif"
]

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
 
 # Occasionally send real media
 if random.random() < 0.45:
 time.sleep(random.uniform(2.5, 6))
 send_tease_media(chat_id)
 
 except:
 bot.send_message(chat_id, "Hahaha~ You're so fucking pathetic 😈")

def send_tease_media(chat_id):
 try:
 media_url = random.choice(tease_media)
 bot.send_photo(chat_id, media_url, caption=random.choice(["💦", "😈", "🖤", "👣"]))
 except:
 pass # Fail silently

print("✅ Mistress Aria - Real Media + Natural Descriptive")
bot.infinity_polling()    
    delay = random.randint(10, 55)
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
        
        # Occasionally send a real photo
        if random.random() < 0.48:
            time.sleep(random.uniform(2.8, 6))
            send_real_tease_photo(chat_id)
            
    except:
        bot.send_message(chat_id, "Hahaha~ You're so fucking pathetic 😈")

def send_real_tease_photo(chat_id):
    try:
        prompts = [
            "seductive goth woman in black lingerie teasing pose, curvy athletic body",
            "perfect female feet high arches soft soles dark red toenails close-up",
            "goth woman bent over showing perfect round ass in tiny black thong",
            "wet naked tall goth woman in shower water dripping down body",
            "dominant goth woman in heels looking down",
            "curvy athletic goth woman spreading legs seductive pose"
        ]
        
        prompt = random.choice(prompts)
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=512&height=768&nologo=true"
        
        bot.send_photo(chat_id, image_url, caption=random.choice(["💦", "😈", "🖤", "👣"]))
    except:
        pass

print("✅ Mistress Aria - Natural Descriptive + Real Photos")
bot.infinity_polling()
