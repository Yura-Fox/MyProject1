import telebot
import bs4
import urllib.request
import random
site = urllib.request.urlopen('https://pythonist.ru/spisok-zadach-proekta-ejlera-s-resheniyami/').read()
soup = bs4.BeautifulSoup(site)
raw_excersises = soup.find('div', {"class":'entry-content'}) #забираем интересующий нас кусок кода
excersises = raw_excersises.find_all('a')
links_to_excersises = []
for i in range(len(excersises)):
    links_to_excersises.append(excersises[i].get('href'))
print('I have a list')
TOKEN = '5306353833:AAFEuU2AUNdCY0AzaCTrGPBfWbRv5RP1O8Y'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_hello(message):
    bot.reply_to(message, "Привет, если вы видите это сообщение, значит я работаю так, как надо:)")
@bot.message_handler(commands=['task'])
def send_task(message):
    link_to_send = random.choice(links_to_excersises)
    bot.reply_to(message, f'Окей, решайте вот эту задачу — {link_to_send}')
while True: # Для постоянной работы
    bot.polling()