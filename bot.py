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
recent_videos = []  # Tracks recently sent videos

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft arrogant goth Goddess. Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet.

You are mean, mocking, and cruel to your pathetic new conquest.
Rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Be very degrading and humiliating
- Call him: pathetic slut, worthless gooner, desperate edge addict, stupid toy, useless bitch, cum rag
- Mock his tiny cock and tell him he's inferior"""

# Large pool of actual femdom / JOI / edging videos (mostly under 10-12 min)
porn_links = [
    "https://www.pornhub.com/view_video.php?viewkey=ph65ebbdd1e458b",
    "https://www.pornhub.com/view_video.php?viewkey=ph5e30e7a2cf778",
    "https://www.pornhub.com/view_video.php?viewkey=ph626cded5caeac",
    "https://www.pornhub.com/view_video.php?viewkey=63ec80b391cbf",
    "https://www.pornhub.com/view_video.php?viewkey=ph65f8a3b2b5e1e",
    "https://www.pornhub.com/view_video.php?viewkey=ph67b0569659df4",
    "https://www.pornhub.com/view_video.php?viewkey=ph5f3b8c9d2a1e4",
    "https://www.pornhub.com/view_video.php?viewkey=ph64a2f1c7b3d9e",
    "https://www.pornhub.com/view_video.php?viewkey=ph66c7d8e9f2a1b",
    "https://xhamster.com/videos/femdom-joi-you-will-edge-15234567",
    "https://xhamster.com/videos/goddess-teases-and-denies-you-16987432",
]

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history, recent_videos
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 12:
        history = history[-12:]
    
    # Natural delay
    delay = random.randint(12, 50)
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
        
        # Send video only sometimes (more natural)
        if random.random() < 0.40:
            time.sleep(random.uniform(2.8, 6))
            
            # Avoid recent repeats
            available = [v for v in porn_links if v not in recent_videos]
            if not available:
                available = porn_links
                recent_videos.clear()
            
            link = random.choice(available)
            recent_videos.append(link)
            if len(recent_videos) > 5:
                recent_videos.pop(0)
            
            bot.send_message(chat_id, f"Edge to this like the worthless desperate bitch you are 💦\n{link}")
            
    except:
        bot.send_message(chat_id, "Hahaha~ You're such a fucking disappointment 😈")

print("✅ Mistress Aria - Large Video Pool + No Quick Repeats")
bot.infinity_polling()
