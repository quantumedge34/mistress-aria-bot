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
recent_videos = []

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft arrogant goth Goddess. Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet.

You are mean, mocking, and cruel to your pathetic new conquest.
Rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Be very degrading and humiliating
- Call him: pathetic slut, worthless gooner, desperate edge addict, stupid toy, useless bitch, cum rag
- Mock his tiny cock and how inferior he is"""

# Large pool of working Femdom / JOI / Edging videos (mostly under 10-12 minutes)
porn_links = [
    "https://www.pornhub.com/view_video.php?viewkey=6782899f06aa7",
    "https://www.pornhub.com/view_video.php?viewkey=66acde3fe8659",
    "https://www.pornhub.com/view_video.php?viewkey=66da156cd7251",
    "https://www.pornhub.com/view_video.php?viewkey=65aade90cd326",
    "https://www.pornhub.com/view_video.php?viewkey=63ec80b391cbf",
    "https://www.pornhub.com/view_video.php?viewkey=ph626cded5caeac",
    "https://www.pornhub.com/view_video.php?viewkey=6595d8c6ed19c",
    "https://www.pornhub.com/view_video.php?viewkey=66ad2f72bdbd5",
    "https://www.pornhub.com/view_video.php?viewkey=670d1ad246340",
    "https://www.pornhub.com/view_video.php?viewkey=691516a609187",
    "https://www.pornhub.com/view_video.php?viewkey=679f84d1be40c",
    "https://www.pornhub.com/view_video.php?viewkey=66edd6493d1ba"
]

@bot.message_handler(func=lambda m: True)
def handle(message):
    global history, recent_videos
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    history.append({"role": "user", "content": user_text})
    if len(history) > 12:
        history = history[-12:]
    
    delay = random.randint(12, 55)
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            temperature=0.92,
            max_tokens=240
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        bot.send_message(chat_id, reply)
        
        # Send video occasionally (30-40% chance)
        if random.random() < 0.38:
            time.sleep(random.uniform(3, 7))
            
            available = [v for v in porn_links if v not in recent_videos[-5:]]
            if not available:
                available = porn_links
                recent_videos.clear()
            
            link = random.choice(available)
            recent_videos.append(link)
            if len(recent_videos) > 8:
                recent_videos.pop(0)
            
            bot.send_message(chat_id, f"Stop wasting my time and edge to this like the pathetic desperate bitch you are 💦\n{link}")
            
    except:
        bot.send_message(chat_id, "Hahaha~ You're such a fucking disappointment 😈")

print("✅ Mistress Aria - Large Video Pool")
bot.infinity_polling()        reply = response.choices[0].message.content.strip()
        
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
