# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import settings
from datetime import date
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', "Меркурий", "Венера", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун", "Плутон"]
planet_dic = {'Mercury' : 'Меркурий', 'Venus' : 'Венера', 'Mars': 'Марс', 'Jupiter' : 'Юпитер', 'Saturn' : 'Сатурн', 'Uranus' : 'Уран', 'Neptune' : 'Нептун', 'Pluto' : 'Плутон'}
const_dic = {'And': 'Андромеда', 'Gem': 'Близнецы', 'UMa': 'Большая Медведица', 'CMa': 'Большой Пёс', 'Lib': 'Весы', 'Aqr': 'Водолей', 'Aur': 'Возничий', 'Lup': 'Волк', 'Boo': 'Волопас', 'Com': 'Волосы Вероники', 'Crv': 'Ворон', 'Her': 'Геркулес', 'Hya': 'Гидра', 'Col': 'Голубь', 'CVn': 'Гончие Псы', 'Vir': 'Дева', 'Del': 'Дельфин', 'Dra': 'Дракон', 'Mon': 'Единорог', 'Ara': 'Жертвенник', 'Pic': 'Живописец', 'Cam': 'Жираф', 'Gru': 'Журавль', 'Lep': 'Заяц', 'Oph': 'Змееносец', 'Ser': 'Змея', 'Dor': 'Золотая Рыба', 'Ind': 'Индеец', 'Cas': 'Кассиопея', 'Car': 'Киль', 'Cet': 'Кит', 'Cap': 'Козерог', 'Pyx': 'Компас', 'Pup': 'Корма', 'Cyg': 'Лебедь', 'Leo': 'Лев', 'Vol': 'Летучая Рыба', 'Lyr': 'Лира', 'Vul': 'Лисичка', 'UMi': 'Малая Медведица', 'Equ': 'Малый Конь', 'LMi': 'Малый Лев', 'CMi': 'Малый Пёс', 'Mic': 'Микроскоп', 'Mus': 'Муха', 'Ant': 'Насос', 'Nor': 'Наугольник', 'Ari': 'Овен', 'Oct': 'Октант', 'Aql': 'Орёл', 'Ori': 'Орион', 'Pav': 'Павлин', 'Vel': 'Паруса', 'Peg': 'Пегас', 'Per': 'Персей', 'For': 'Печь', 'Aps': 'Райская Птица', 'Cnc': 'Рак', 'Cae': 'Резец', 'Psc': 'Рыбы', 'Lyn': 'Рысь', 'CrB': 'Северная Корона', 'Sex': 'Секстант', 'Ret': 'Сетка', 'Sco': 'Скорпион', 'Scl': 'Скульптор', 'Men': 'Столовая Гора', 'Sge': 'Стрела', 'Sgr': 'Стрелец', 'Tel': 'Телескоп', 'Tau': 'Телец', 'Tri': 'Треугольник', 'Tuc': 'Тукан', 'Phe': 'Феникс', 'Cha': 'Хамелеон', 'Cen': 'Центавр ', 'Cep': 'Цефей', 'Cir': 'Циркуль', 'Hor': 'Часы', 'Crt': 'Чаша', 'Sct': 'Щит', 'Eri': 'Эридан', 'Hyi': 'Южная Гидра', 'CrA': 'Южная Корона', 'PsA': 'Южная Рыба', 'Cru': 'Южный Крест', 'TrA': 'Южный Треугольник', 'Lac': 'Ящерица'}


def planet(bot,update):
    text = 'Вызван /planet'
    print(text)
    #update.message.reply_text(text)
    today = str(date.today())
    today.replace('-', '/')
    user_text = update.message.text 
    print(user_text)
    user_list = user_text.split(' ')
    for plan in user_list:
        if plan in planet_list:
            if planet_list.index(plan)>7:
                plan=planet_list[planet_list.index(plan)-8]
            planet_object = getattr(ephem, plan)
            res = planet_object(today)
            ephem.constellation(res)
            update.message.reply_text(ephem.constellation(res))
            update.message.reply_text(planet_dic[plan] + ' сегодня в созвездии '+ const_dic[ephem.constellation(res)[0]])


def main():
    mybot =Updater(settings.KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()