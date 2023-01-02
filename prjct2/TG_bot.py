import telebot
from telebot import types
from parsing import main_parsing

anecdotes = []


bot = telebot.TeleBot('5961918704:AAGXSt7ZduB9X8lD4DqQoRYAifBvzQstbIw')


@bot.message_handler(commands = ["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет. Этот бот выдает анекдоты, для более подробной информации наберите /help')


# Функция, обрабатывающая команду /help
@bot.message_handler(commands = ["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'После команды /find бот ищет анекдоты '
    'на www.anekdot.ru. Следует написать /find. ')


# Функция, обрабатывающая команду /find
@bot.message_handler(commands=["find"])
def start(m, res=False):
    global anecdotes

    bot.send_message(m.chat.id, 'Ожидайте...')

    # парсим www.anekdot.ru
    anecdotes = main_parsing()

    bot.send_message(m.chat.id, anecdotes[0] + ' /next')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Следующий анекдот")
    markup.add(item)


@bot.message_handler(commands=["next"])
def start(m, res=False):
    global anecdotes

    try:
        # пробуем удалить 1 элемент и вывести следующий
        anecdotes.pop(0)
        bot.send_message(m.chat.id, anecdotes[0] + ' /next')
    except:
        # если это невозможно пишем, что анекдотов больше нет
        bot.send_message(m.chat.id, 'На сегодня анекдоты закончились, приходи завтра!')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):

    bot.send_message(message.chat.id, 'Вы можете ознакомится с функционалом '
    'бота с помощью команды /help')



# Запускаем бота
bot.infinity_polling()
