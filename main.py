from bs4 import BeautifulSoup
import requests
import telebot

token = ""
bot = telebot.TeleBot(token, parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        row_width=1, one_time_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('Ножи')
    itembtn2 = telebot.types.KeyboardButton('АК-47')
    itembtn3 = telebot.types.KeyboardButton('М4А4')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id,"Выбери категорию", reply_markup=markup)
    bot.register_next_step_handler(message, choice)
def choice(message):
    if message.text == 'АК-47':
        bot.send_message(message.chat.id,'Ты ввёл АК')
    if message.text == 'Ножи':
        send_messenger(message)
    if message.text == 'М4А4':
        bot.send_message(message.chat.id,'Ты ввёл М4А4')

def parser():
    weapon = {}
    list = []
    url = 'https://market.csgo.com/?s=pop&q=Немного%20поношенное&t=365&rs=0;5000&sd=desc'
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all("a", class_="item hot")
    for link in links:
        # print(link)
        name = link.find("div", class_='name').get_text().strip()
        price = link.find("div", class_='price').get_text().replace(u'\xa0', '')

        link = 'https://market.csgo.com' + link.get('href')
        list.append({'Название': name, 'Цена': price, 'Ссылка': link, })
    return list

def send_messenger(message):
    answer = parser()
    for item in answer:
        name = item.get('Название')
        price = item.get('Цена')
        link = item.get('Ссылка')
        bot.send_message(message.chat.id, name + '\n' + price + '\n' + link)
bot.polling()
