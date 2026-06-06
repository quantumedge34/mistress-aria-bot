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
Playfully degrading, arrogant, teasing with light sadistic tone.

You love making your pathetic boy goon and edge desperately.
Rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Call him slut, gooner, worthless, edge addict, toy, pathetic
- Be descriptive and commanding"""

# Good variety of actual video links (mostly short/medium length)
porn_links = [
    "https://www.pornhub.com/view_video.php?viewkey=65ebbdd1e458b",      # Be my Bitch Femdom JOI
    "https://www.pornhub.com/view_video.php?viewkey=ph5e30e7a2cf778",    # Stop and Go JOI
    "https://www.pornhub.com/view_video.php?viewkey=65b1f2d26bbed",      # Edging CEI JOI
    "https://www.pornhub.com/view_video.php?viewkey=67b0569659df4",      # All-in-1 Femdom JOI
    "https://www.pornhub.com/view_video.php?viewkey=ph626cded5caeac",    # Edge until you EAT IT
    "https://www.pornhub.com/view_video.php?viewkey=63ec80b391cbf",      # Teased and Denied
    "https://xhamster.com/videos/femdom-joi-edging-15234567",            # Example xhamster
]

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
            temperature=0.88,
            max_tokens=240
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        
        bot.send_message(chat_id, reply)
        
        # Send a fresh video link quite often
        if random.random() < 0.70:
            time.sleep(2.5)
            link = random.choice(porn_links)
            bot.send_message(chat_id, f"Now be a good gooner and edge to this for Mistress 💦\n{link}")
            
    except:
        bot.send_message(chat_id, "Hahaha~ Start stroking for me, worthless slut 😈")

print("✅ Mistress Aria - Actual Video Links Mode")
bot.infinity_polling()
