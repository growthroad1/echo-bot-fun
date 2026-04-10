import telebot
import random

TOKEN = "8412479404:AAHSvPxQ-hkAsb39wQN-oAGBuBxsDraOUXk"

bot = telebot.TeleBot(TOKEN)

# Списки для "приколов" при повторении
prefixes = ["", "Ого, ", "Серьёзно? ", "Хаха, ", "Понял тебя: ", "Копи-паст: ", "Так и запишем: "]
suffixes = [" 😂", " 🔥", " 👍", " 👀", " 😎", " ✨", " 🤖"]
additions = [
    " (я это уже где-то слышал)",
    " (гениально!)",
    " (записал в блокнот)",
    " (мой любимый фразон)",
    ""
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
        "Привет! 👋\n\n"
        "Я — бот-эхо с характером.\n"
        "Пиши мне что угодно — я буду повторять это, но с душой и приколом.\n\n"
        "Попробуй написать что-нибудь!")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Просто пиши мне любой текст — я его красиво повторю с эмодзи и шутками.")

@bot.message_handler(func=lambda message: True)
def echo_with_style(message):
    if not message.text:
        bot.reply_to(message, "Я понимаю только текст пока что 😔")
        return

    original = message.text.strip()
    
    # Делаем интересное повторение
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    addition = random.choice(additions)
    
    # Иногда меняем регистр для прикола
    if random.random() > 0.7:
        echoed = original.upper()
    elif random.random() > 0.7:
        echoed = original.lower()
    else:
        echoed = original
    
    response = f"{prefix}{echoed}{suffix}{addition}"
    
    bot.reply_to(message, response)

if __name__ == "__main__":
    print("Эхо-бот с характером запущен...")
    bot.infinity_polling()