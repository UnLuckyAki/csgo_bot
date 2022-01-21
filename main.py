from bs4 import BeautifulSoup
import requests
import telebot
import time


token = "ВАШТОКЕН"

bot = telebot.TeleBot(token, parse_mode=None)
def guns(message):
    url = 'https://market.csgo.com/'
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all("a", class_="item hot")

    for link in links:
        link = 'https://market.csgo.com'+ link.get('href')
        #price = link.find('div', class_='price').text + 'Р'
        #answer = link +'\n' + price
        bot.send_message(message.chat.id, link)
        time.sleep(1)
@bot.message_handler(commands=['guns'])
def send_welcome(message):
    guns(message)


bot.polling()
