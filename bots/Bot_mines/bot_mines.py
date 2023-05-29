import time
import random
import json,requests
import telebot
from datetime import datetime
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import bd


api_key = '6295353140:AAHihnqorDq6y0bITUv60hnL23V2Pq7PHLY' # Neste campo tenho que colocar a API do BotFather!
chat_id = '-1001875843199' # Neste campo tenho que colocar o ID do meu canal!

bot = telebot.TeleBot(token=api_key)

def ALERT_GALE1():
    h = datetime.now().hour
    m = datetime.now().minute+1
    s = datetime.now().second
    if h <= 9:
        h =  f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    message_id = bot.send_message(chat_id=chat_id, text=f'''NOVA ENTRADA EM {h}:{m}:{s} GERANDO ENTRADA...''' ).message_id
    bd.message_ids1 = message_id
    bd.message_delete1 = True
    return

def DELETE_GALE1():
    if bd.message_delete1 == True:
        bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1)
        bd.message_delete1 = False

while True:
    h = datetime.now().hour
    m = datetime.now().minute+2
    s = datetime.now().second
    if h <= 9:
        h =  f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')
    cores = ['⭐','🟦','🟦','🟦','🟦','🟦','🟦','🟦','🟦','🟦','⭐','🟦','🟦','🟦','🟦','⭐','🟦','🟦','🟦','🟦','⭐','🟦','🟦','🟦','🟦']

    for i in range (25):
        sample = random.sample(cores, k=25)
        print(sample[0], sample[1], sample[2], sample[3], sample[4], sample[5], sample[6], sample[7], sample[8],sample[9], sample[10], sample[11], sample[12], sample[13], sample[14], sample[15], sample[16], sample[17], sample[18], sample[19], sample[20], sample[21], sample[22], sample[23], sample[24])

        def button_link():

            markup = InlineKeyboardMarkup()

            markup.row_width = 2

            markup.add(InlineKeyboardButton(text=f"📲 Cadastre-se", url="https://bit.ly/MinesBotOficiall"))
            return markup

    dados = bot.send_message(chat_id=chat_id, text=(f'''
🤑 𝗦𝗜𝗡𝗔𝗟 𝗖𝗢𝗡𝗙𝗜𝗥𝗠𝗔𝗗𝗢!
💣 Minas: 4
🔁 Nº de tentativas: 3

⬇️ Depósito Mínimo: R$2,00 ⬇️
🎰 𝗖𝗮𝗱𝗮𝘀𝘁𝗿𝗲-𝘀𝗲: https://bit.ly/MinesBotOficiall
 🖥 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://bit.ly/MinesBotOficiall
⬆️ Depósito Mínimo: R$2,00 ⬆️

🚨 FUNCIONA APENAS NA PLATAFORMA ACIMA!
⚠️ NÃO TENTE EM OUTRO SITE!
{random.choice(sample[0])}{random.choice(sample[1])}{random.choice(sample[2])}{random.choice(sample[3])}{random.choice(sample[4])}
{random.choice(sample[5])}{random.choice(sample[6])}{random.choice(sample[7])}{random.choice(sample[8])}{random.choice(sample[9])}
{random.choice(sample[10])}{random.choice(sample[11])}{random.choice(sample[12])}{random.choice(sample[13])}{random.choice(sample[14])}
{random.choice(sample[15])}{random.choice(sample[16])}{random.choice(sample[17])}{random.choice(sample[18])}{random.choice(sample[19])}
{random.choice(sample[20])}{random.choice(sample[21])}{random.choice(sample[22])}{random.choice(sample[23])}{random.choice(sample[24])}
⏱ 𝙑𝙖́𝙡𝙞𝙙𝙤 𝙖𝙩𝙚́: {h}:{m}:{s}  '''),
                reply_markup=button_link()) #acima é a mensagem que será exibida no telegram!
    time.sleep(120)# Aqui é a duração do sinal no caso é 2 minutos, 120 segundos!
    bot . edit_message_text(f'''
    ⭐𝙎𝙞𝙣𝙖𝙡 𝙛𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙙𝙤⭐
    ⭐Mines⭐
    ⏱𝙁𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙙𝙤 𝙖́𝙨: {h}:{m}:{s}
    ''', dados . chat . id , dados . message_id)# Aqui o bot deleta a mensagem anterior para ficar mais clean!
    
    time.sleep(60)#60
    ALERT_GALE1()
    time.sleep(10)#10
    DELETE_GALE1()
    time.sleep(50)#50


