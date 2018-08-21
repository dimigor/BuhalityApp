import telebot
from config import config
import app


bot = telebot.TeleBot(config.TOKEN)
person = {}


@bot.message_handler(commands=["start"])
def get_name_messages(message):
    bot.send_message(message.chat.id, "Hello")


@bot.message_handler(regexp=config.REGEXP)
def handle_message(message):

    list_message = message.text.split()

    for item in list_message[+1:]:
        if item not in person.keys():
            person.update({item: app.Person(item)})

    person[list_message[1]].paid(int(list_message[0]), *person.values())
    for key in person:

        strings = "Name - {}\nSpent Money - {}\nMoney paid - {}\nMoney borrow - {}\n".format(
            person[key].name, person[key].Money.money, person[key].Money.paid, person[key].borrow)
        strings += "------\n"

        bot.send_message(message.chat.id, strings)


if __name__ == "__main__":

    bot.polling(none_stop=True, interval=0)
