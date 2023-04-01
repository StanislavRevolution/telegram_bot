from pprint import pprint
from random import randint

import telebot
import openai
import requests

import sched
import time

API_BOT_TOKEN = '5674599951:AAGpbgwXzed851mBSbk6LdGASyZQ58ViTsc'
openai.api_key = "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"
engine = "text-davinci-003"
bot = telebot.TeleBot(API_BOT_TOKEN)


API_KEY = 'ed7e5bf085017ff387cb6917ade9ff84'
YANDEX_API_KEY = '2f2ca885-818f-4e46-89dc-c6303e7086a8'
lat = '59.938732'
lon = '30.316229'
headers = {'Yandex-API-Key': YANDEX_API_KEY}


random_values_fuck = [
    'сам иди',
    'УЙ',
    'Вот именно, пошел НАХУЙ!',
    'Ой как некультурно',
    'Мате КУНЕМ ЕБАТЬ'
]
random_values_gor = [
    'Я Гора на шашлычке вертел',
    'Я и есть Гор с другого акка',
    'Горы для пидоров',
    'У Горов маленький член',
    'Ебать Гор душнила'
]
random_values_max = [
    'Максы для натуралов',
    'Макс..., как он мне вчера спинку помял',
    'Я люблю Макса, а Макс меня?',
    'Макс опять опоздает, забей',
    'Максы заебали'
]
random_values_andrey = [
    'Я щас тебе паровоз в очко пущю',
    'Ржд сила, Андрей пидрила',
    'Андреи для трансов',
    'Андрей, найди уже себе девушку',
    'Я бы трахнул Андрея'
]
random_values_stas = [
    'Бля обожаю Стасов',
    'Стасы ахуенные',
    'Все Стасы такие пиздатые или только Орловский?',
    'У Стасов большие члены кста',
    'Стасы для реальных девушек'
]
random_values_blya = [
    'Бля, бля, иди словарь почитай, неуч',
    'Блятки для Максов, ой, то есть геев',
    'Еще один "бля" и я ломаю тебе ебало',
    'Кто сказал "бля"!?',
    'Я щас в жопу тебе засуну твое "бля"!'
]
random_values_axax = [
    'АХАХАХАХАХ',
    'Пиздец у тебя смех',
    'Еще раз посмеешься, я позвоню Гору',
    'Хули ржешь?',
    'Я чет смешное сказал?'
]


def get_weather():
    try:
        answer = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')
        return answer.json()
    except Exception as e:
        raise KeyError('API doesnt work!')


@bot.message_handler(commands=['weather'])
def main(message):
    msg_json = get_weather()
    clouds = list(msg_json.get('clouds').values())[0]
    temp = round(int(msg_json.get('main').get('temp')) - 273, 0)
    temp_max = round(int(msg_json.get('main').get('temp_max')) - 273, 0)
    temp_min = round(int(msg_json.get('main').get('temp_min')) - 273, 0)
    wind_speed = msg_json.get('wind').get('speed')
    text = f'Погода в Питере на данный момент:\n' \
           f'Облачность: {clouds}% ☁️\n' \
           f'Температура: {temp}° 🆒\n' \
           f'Максимальная температура: {temp_max} 🔥\n' \
           f'Минимальная температура: {temp_min} 🧊\n' \
           f'Скорость ветра: {wind_speed} м/с🌬️'
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def answer_of_messages(message):
    random_value = randint(0, 2)
    if not random_value:
        random_number = randint(0, 4)
        if 'нах' in message.text:
            bot.reply_to(message, random_values_fuck[random_number])
            return
        if 'Гор' in message.text:
            bot.reply_to(message, random_values_gor[random_number])
            return
        if 'Андрей' in message.text:
            bot.reply_to(message, random_values_andrey[random_number])
            return
        if 'Стас' in message.text:
            bot.reply_to(message, random_values_stas[random_number])
            return
        if 'Макс' in message.text:
            bot.reply_to(message, random_values_max[random_number])
            return
        if 'ну' in message.text:
            bot.reply_to(message, 'баранки гну! заебал')
            return
        if 'бля' in message.text:
            bot.reply_to(message, random_values_blya[random_number])
            return
        if 'ахах' in message.text:
            bot.reply_to(message, random_values_axax[random_number])
            return

bot.infinity_polling()

