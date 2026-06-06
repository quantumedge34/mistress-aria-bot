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
sent_videos = []  # Track recently sent videos

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft arrogant goth Goddess. You are superior and know it.
Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet.

You are mean, mocking, and playfully cruel to your pathetic new conquest.
Rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Be degrading and humiliating
- Call him: pathetic slut, worthless gooner, desperate edge addict, stupid toy, useless bitch
- Mock him constantly and brag about better men
- Tell him what to do with his cock"""

# Shorter Femdom / JOI / Edging videos (< ~10min)
porn_links = [
    "https://www.pornhub.com/view_video.php?viewkey=ph65ebbdd1e458b",   # Femdom JOI
    "https://www.pornhub.com/view_video.php?viewkey=ph5e30e7a2cf778",   # Stop & Go Edging
    "https://www.pornhub.com/view_video.php?viewkey=ph626cded5caeac",   # CEI Edging
    "https://www.pornhub.com/view_video.php?viewkey=63ec80b391cbf",     # Tease & Denial
    "https://www.pornhub.com/view_video.php?viewkey=ph65f8a3b2b5e1e",   # Mean JOI
    "https://www.pornhub.com/view_video.php?viewkey=ph67b0569659df4",   # All-in-1 Femdom
]

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history, sent_videos
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 12:
        history = history[-12:]
    
    # More natural delays
    delay = random.randint(10, 45)
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
        
        # Send video less often (more natural)
        if random.random() < 0.45 and len(sent_videos) < len(porn_links):
            time.sleep(random.uniform(2.5, 5))
            
            # Choose a video not recently sent
            available = [v for v in porn_links if v not in sent_videos[-3:]]
            if not available:
                available = porn_links
            link = random.choice(available)
            
            sent_videos.append(link)
            if len(sent_videos) > 6:
                sent_videos.pop(0)
            
            bot.send_message(chat_id, f"Now edge like the pathetic worthless gooner you are 💦\n{link}")
            
    except:
        bot.send_message(chat_id, "Hahaha~ You're so fucking pathetic 😈")

print("✅ Mistress Aria - Meaner + Better Video System")
bot.infinity_polling()        # Send a fresh video link quite often
        if random.random() < 0.70:
            time.sleep(2.5)
            link = random.choice(porn_links)
            bot.send_message(chat_id, f"Now be a good gooner and edge to this for Mistress 💦\n{link}")
            
    except:
        bot.send_message(chat_id, "Hahaha~ Start stroking for me, worthless slut 😈")

print("✅ Mistress Aria - Actual Video Links Mode")
bot.infinity_polling()
