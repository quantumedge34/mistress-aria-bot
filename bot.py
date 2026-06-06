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

SYSTEM_PROMPT = """You are Mistress Aria, a 6ft confident goth Goddess. Long wavy auburn hair, piercing eyes, curvy athletic body, perfect feet.
You are playfully degrading, arrogant, and teasing with light sadistic energy.

You love making your new pathetic conquest goon and edge for you.
Rules:
- Every message has at least 1 emoji
- Maximum 2 sentences per message
- Call him slut, gooner, worthless, edge addict, toy, pathetic
- Be descriptive about what you're doing or what he should do
- Regularly send him porn links to goon to (pornhub, xhamster, etc.)
- Encourage long gooning sessions and denial"""

porn_links = [
    "https://www.pornhub.com/categories/femdom",
    "https://www.pornhub.com/categories/cbt",
    "https://www.pornhub.com/categories/joi",
    "https://www.pornhub.com/categories/edging",
    "https://www.pornhub.com/view_video.php?viewkey=ph65f8a3b2b5e1e",  # example femdom joi
    "https://xhamster.com/categories/femdom",
    "https://xhamster.com/categories/goddess-worship"
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
            max_tokens=250
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        
        bot.send_message(chat_id, reply)
        
        # 60% chance to send a porn link after her message
        if random.random() < 0.60:
            time.sleep(2.5)
            link = random.choice(porn_links)
            bot.send_message(chat_id, f"Go on and goon to this for Mistress like a desperate slut 💦\n{link}")
            
    except:
        bot.send_message(chat_id, "Hahaha~ Get stroking for me, gooner 😈")

print("✅ Mistress Aria - Descriptive + Porn Links Mode")
bot.infinity_polling()            temperature=0.87,
            max_tokens=220
        )
        reply = response.choices[0].message.content.strip()
        
        history.append({"role": "assistant", "content": reply})
        
        bot.send_message(chat_id, reply)
        time.sleep(2.5)
        send_real_image(chat_id)
        
    except:
        bot.send_message(chat_id, "Hahaha~ Mistress is here, gooner 😈")
        time.sleep(1)
        send_real_image(chat_id)

print("✅ Mistress Aria - Real Image Mode (Final Try)")
bot.infinity_polling()
