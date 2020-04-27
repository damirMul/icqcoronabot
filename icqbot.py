import json
from bot.bot import Bot
from bot.handler import MessageHandler, BotButtonCommandHandler, Filter
from sqldb import add_user, check
import pandas as pd
from config import TOKEN


bot = Bot(token=TOKEN)


def buttons_answer_cb(bot, event) :
    cases = pd.read_csv('cases.csv', sep=",", index_col='Country/Other')
    if event.data['callbackData']=="call_back_id_1" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Украина\n\n"
                 f"Заболевших: {cases.loc['Ukraine', 'Total Cases']} ({cases.loc['Ukraine', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Ukraine', 'Total Deaths']}({cases.loc['Ukraine', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Ukraine', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Ukraine', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_2" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Казахстан\n\n"
                 f"Заболевших: {cases.loc['Kazakhstan', 'Total Cases']} ({cases.loc['Kazakhstan', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Kazakhstan', 'Total Deaths']}({cases.loc['Kazakhstan', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Kazakhstan', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Kazakhstan', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_3" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Россия\n\n"
                 f"Заболевших: {cases.loc['Russia', 'Total Cases']} ({cases.loc['Russia', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Russia', 'Total Deaths']}({cases.loc['Russia', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Russia', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Russia', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_4" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Белоруссия\n\n"
                 f"Заболевших: {cases.loc['Belarus', 'Total Cases']} ({cases.loc['Belarus', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Belarus', 'Total Deaths']}({cases.loc['Belarus', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Belarus', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Belarus', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_5" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: США\n\n"
                 f"Заболевших: {cases.loc['USA', 'Total Cases']} ({cases.loc['USA', 'New Cases']})\n"
                 f"Смертей: {cases.loc['USA', 'Total Deaths']}({cases.loc['USA', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['USA', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['USA', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_6" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Италия\n\n"
                 f"Заболевших: {cases.loc['Italy', 'Total Cases']} ({cases.loc['Italy', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Italy', 'Total Deaths']}({cases.loc['Italy', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Italy', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Italy', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_7" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Испания\n\n"
                 f"Заболевших: {cases.loc['Spain', 'Total Cases']} ({cases.loc['Spain', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Spain', 'Total Deaths']}({cases.loc['Spain', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Spain', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Spain', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_8" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Франция\n\n"
                 f"Заболевших: {cases.loc['France', 'Total Cases']} ({cases.loc['France', 'New Cases']})\n"
                 f"Смертей: {cases.loc['France', 'Total Deaths']}({cases.loc['France', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['France', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['France', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_9" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Германия\n\n"
                 f"Заболевших: {cases.loc['Germany', 'Total Cases']} ({cases.loc['Germany', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Germany', 'Total Deaths']}({cases.loc['Germany', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Germany', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Germany', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_10" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Великобритания \n\n"
                 f"Заболевших: {cases.loc['UK', 'Total Cases']} ({cases.loc['UK', 'New Cases']})\n"
                 f"Смертей: {cases.loc['UK', 'Total Deaths']}({cases.loc['UK', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['UK', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['UK', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_11" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Китай \n\n"
                 f"Заболевших: {cases.loc['China', 'Total Cases']} ({cases.loc['China', 'New Cases']})\n"
                 f"Смертей: {cases.loc['China', 'Total Deaths']}({cases.loc['China', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['China', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['China', 'Total Tests']}",
            show_alert=True
        )
    elif event.data['callbackData']=="call_back_id_12" :
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=f"Данные по стране: Канада \n\n"
                 f"Заболевших: {cases.loc['Canada', 'Total Cases']} ({cases.loc['Canada', 'New Cases']})\n"
                 f"Смертей: {cases.loc['Canada', 'Total Deaths']}({cases.loc['Canada', 'New Deaths']})\n"
                 f"Выздоровело: {cases.loc['Canada', 'Total Recovered']}\n"
                 f"Протестировано: {cases.loc['Canada', 'Total Tests']}",
            show_alert=True
        )


def message_cb(bot, event) :
    cases = pd.read_csv('cases.csv', sep=",", index_col='Country/Other')
    bot.send_text(chat_id=event.data['chat']['chatId'],
                  text=f"Данные о заболевших COVID-19 по всему миру🌎:\n" \
                       f"Заболевших: {cases.loc['World', 'Total Cases']} ({cases.loc['World', 'New Cases']})\n" \
                       f"Смертей: {cases.loc['World', 'Total Deaths']} ({cases.loc['World', 'New Deaths']})\n" \
                       f"Выздоровело: {cases.loc['World', 'Total Recovered']}\n\n" \
                       f"Выберите страну из списка или отправьте сообщение с названием страны ",
                  inline_keyboard_markup="{}".format(json.dumps([[
                      {"text" : "Россия 🇷🇺", "callbackData" : "call_back_id_3", "style" : "primary"},
                      {"text" : "Казахстан 🇰🇿", "callbackData" : "call_back_id_2", "style" : "primary"}],
                      [{"text" : "Украина 🇺🇦", "callbackData" : "call_back_id_1", "style" : "primary"},
                       {"text" : "Белорусь 🇧🇾", "callbackData" : "call_back_id_4", "style" : "primary"}],
                      [{"text" : "США 🇺🇸", "callbackData" : "call_back_id_5", "style" : "primary"},
                       {"text" : "Италия 🇮🇹", "callbackData" : "call_back_id_6", "style" : "primary"}],
                      [{"text" : "Испания 🇪🇸", "callbackData" : "call_back_id_7", "style" : "primary"},
                       {"text" : "Франция 🇫🇷", "callbackData" : "call_back_id_8", "style" : "primary"}],
                      [{"text" : "Германия 🇩🇪", "callbackData" : "call_back_id_9", "style" : "primary"},
                       {"text" : "Великобритания 🇬🇧", "callbackData" : "call_back_id_10", "style" : "primary"}],
                      [{"text" : "Китай 🇨🇳", "callbackData" : "call_back_id_11", "style" : "primary"},
                       {"text" : "Канада 🇨🇦", "callbackData" : "call_back_id_12", "style" : "primary"}]

                  ]))),

    if check(event.message_author['userId'])==1 :
        print(event.message_author),
    else :
        add_user(
            userId=event.message_author['userId'],
            nick=event.message_author['nick'],
            firstName=event.message_author['firstName'],
            lastName=event.message_author['lastName']
        )


def message_stats(bot, event) :
    cases = pd.read_csv('cases.csv', sep=",", index_col='Country/Other')
    message = event.text
    if message=="США" :
        id = 'USA'
    elif message=="Испания" :
        id = 'Spain'
    elif message=="Италия" :
        id = 'Italy'
    elif message=="Франция" :
        id = 'France'
    elif message=="Германия" :
        id = 'Germany'
    elif message=="Великобритания" :
        id = 'UK'
    elif message=="Турция" :
        id = 'Turkey'
    elif message=="Иран" :
        id = 'Iran'
    elif message=="Китай" :
        id = 'China'
    elif message=="Россия" :
        id = 'Russia'
    elif message=="Бразилия" :
        id = 'Brazil'
    elif message=="Бельгия" :
        id = 'Belgium'
    elif message=="Канада" :
        id = 'Canada'
    elif message=="Нидерланды" :
        id = 'Netherlands'
    elif message=="Швейцария" :
        id = 'Switzerland'
    elif message=="Португалия" :
        id = 'Portugal'
    elif message=="Индия" :
        id = 'India'
    elif message=="Перу" :
        id = 'Peru'
    elif message=="Ирландия" :
        id = 'Ireland'
    elif message=="Швеция" :
        id = 'Sweden'
    elif message=="Австрия" :
        id = 'Austria'
    elif message=="Израиль" :
        id = 'Israel'
    elif message=="Саудовская Аравия" :
        id = 'Saudi Arabia'
    elif message=="Япония" :
        id = 'Japan'
    elif message=="Чили" :
        id = 'Chile'
    elif message=="Сингапур" :
        id = 'Singapore'
    elif message=="Эквадор" :
        id = 'Ecuador'
    elif message=="Южная Корея" :
        id = 'S. Korea'
    elif message=="Мексика" :
        id = 'Mexico'
    elif message=="Пакистан" :
        id = 'Pakistan'
    elif message=="Польша" :
        id = 'Poland'
    elif message=="Румыния" :
        id = 'Romania'
    elif message=="ОАЭ" :
        id = 'UAE'
    elif message=="Дания" :
        id = 'Denmark'
    elif message=="Индонезия" :
        id = 'Indonesia'
    elif message=="Катар" :
        id = 'Qatar'
    elif message=="Норвегия" :
        id = 'Norway'
    elif message=="Беларусь" :
        id = 'Belarus'
    elif message=="Украина" :
        id = 'Ukraine'
    elif message=="Чехия" :
        id = 'Czechia'
    elif message=="Сербия" :
        id = 'Serbia'
    elif message=="Филиппины" :
        id = 'Philippines'
    elif message=="Австралия" :
        id = 'Australia'
    elif message=="Малайзия" :
        id = 'Malaysia'
    elif message=="Панама" :
        id = 'Panama'
    elif message=="Колумбия" :
        id = 'Colombia'
    elif message=="Финляндия" :
        id = 'Finland'
    elif message=="Бангладеш" :
        id = 'Bangladesh'
    elif message=="Египет" :
        id = 'Egypt'
    elif message=="Люксембург" :
        id = 'Luxembourg'
    elif message=="Марокко" :
        id = 'Morocco'
    elif message=="Аргентина" :
        id = 'Argentina'
    elif message=="Алжир" :
        id = 'Algeria'
    elif message=="Таиланд" :
        id = 'Thailand'
    elif message=="Молдова" :
        id = 'Moldova'
    elif message=="Греция" :
        id = 'Greece'
    elif message=="Кувейт" :
        id = 'Kuwait'
    elif message=="Венгрия" :
        id = 'Hungary'
    elif message=="Казахстан" :
        id = 'Kazakhstan'
    elif message=="Бахрейн" :
        id = 'Bahrain'
    elif message=="Хорватия" :
        id = 'Croatia'
    elif message=="Исландия" :
        id = 'Iceland'
    elif message=="Оман" :
        id = 'Oman'
    elif message=="Узбекистан" :
        id = 'Uzbekistan'
    elif message=="Ирак" :
        id = 'Iraq'
    elif message=="Эстония" :
        id = 'Estonia'
    elif message=="Армения" :
        id = 'Armenia'
    elif message=="Азербайджан" :
        id = 'Azerbaijan'
    elif message=="Новая Зеландия" :
        id = 'New Zealand'
    elif message=="Литва" :
        id = 'Lithuania'
    elif message=="Словения" :
        id = 'Slovenia'
    elif message=="Словакия" :
        id = 'Slovakia'
    elif message=="Афганистан" :
        id = 'Afghanistan'
    elif message=="Куба" :
        id = 'Cuba'
    elif message=="Камерун" :
        id = 'Cameroon'
    elif message=="Гана" :
        id = 'Ghana'
    elif message=="Болгария" :
        id = 'Bulgaria'
    elif message=="Гонконг" :
        id = 'Hong Kong'
    elif message=="Джибути" :
        id = 'Djibouti'
    elif message=="Тунис" :
        id = 'Tunisia'
    elif message=="Нигерия" :
        id = 'Nigeria'
    elif message=="Кипр" :
        id = 'Cyprus'
    elif message=="Латвия" :
        id = 'Latvia'
    elif message=="Гвинея" :
        id = 'Guinea'
    elif message=="Андорра" :
        id = 'Andorra'
    elif message=="Ливан" :
        id = 'Lebanon'
    elif message=="Коста Рика" :
        id = 'Costa Rica'
    elif message=="Боливия" :
        id = 'Bolivia'
    elif message=="Албания" :
        id = 'Albania'
    elif message=="Нигер" :
        id = 'Niger'
    elif message=="Киргизия" :
        id = 'Kyrgyzstan'
    elif message=="Буркина-Фасо" :
        id = 'Burkina Faso'
    elif message=="Уругвай" :
        id = 'Uruguay'
    elif message=="Гондурас" :
        id = 'Honduras'
    elif message=="Сан-Марино" :
        id = 'San Marino'
    elif message=="Палестина" :
        id = 'Palestine'
    elif message=="Сенегал" :
        id = 'Senegal'
    elif message=="Мальта" :
        id = 'Malta'
    elif message=="Иордания" :
        id = 'Jordan'
    elif message=="Тайвань" :
        id = 'Taiwan'
    elif message=="Грузия" :
        id = 'Georgia'
    elif message=="Гватемала" :
        id = 'Guatemala'
    elif message=="Шри-Ланка" :
        id = 'Sri Lanka'
    elif message=="Маврикий" :
        id = 'Mauritius'
    elif message=="Майотта" :
        id = 'Mayotte'
    elif message=="Черногория" :
        id = 'Montenegro'
    elif message=="Кения" :
        id = 'Kenya'
    elif message=="Венесуэла" :
        id = 'Venezuela'
    elif message=="Мали" :
        id = 'Mali'
    elif message=="Сомали" :
        id = 'Somalia'
    elif message=="Танзания" :
        id = 'Tanzania'
    elif message=="Вьетнам" :
        id = 'Vietnam'
    elif message=="Ямайка" :
        id = 'Jamaica'
    elif message=="Сальвадор" :
        id = 'El Salvador'
    elif message=="Парагвай" :
        id = 'Paraguay'
    elif message=="Фарерские острова" :
        id = 'Faeroe Islands'
    elif message=="Конго" :
        id = 'Congo'
    elif message=="Габон" :
        id = 'Gabon'
    elif message=="Мартиника" :
        id = 'Martinique'
    elif message=="Судан" :
        id = 'Sudan'
    elif message=="Руанда" :
        id = 'Rwanda'
    elif message=="Гваделупа" :
        id = 'Guadeloupe'
    elif message=="Бруней" :
        id = 'Brunei'
    elif message=="Гибралтар" :
        id = 'Gibraltar'
    elif message=="Мьянма" :
        id = 'Myanmar'
    elif message=="Камбоджа" :
        id = 'Cambodia'
    elif message=="Мадагаскар" :
        id = 'Madagascar'
    elif message=="Эфиопия" :
        id = 'Ethiopia'
    elif message=="Либерия" :
        id = 'Liberia'
    elif message=="Аруба" :
        id = 'Aruba'
    elif message=="Бермудские острова" :
        id = 'Bermuda'
    elif message=="Монако" :
        id = 'Monaco'
    elif message=="Мальдивы" :
        id = 'Maldives'
    elif message=="Того" :
        id = 'Togo'
    elif message=="Лихтенштейн" :
        id = 'Liechtenstein'
    elif message=="Барбадос" :
        id = 'Barbados'
    elif message=="Замбия" :
        id = 'Zambia'
    elif message=="Синт-Мартен" :
        id = 'Sint Maarten'
    elif message=="Кабо Верде" :
        id = 'Cabo Verde'
    elif message=="Багамские острова" :
        id = 'Bahamas'
    elif message=="Гайана" :
        id = 'Guyana'
    elif message=="Каймановы острова" :
        id = 'Cayman Islands'
    elif message=="Уганда" :
        id = 'Uganda'
    elif message=="Гаити" :
        id = 'Haiti'
    elif message=="Сьерра-Леоне" :
        id = 'Sierra Leone'
    elif message=="Ливия" :
        id = 'Libya'
    elif message=="Бенин" :
        id = 'Benin'
    elif message=="Непал" :
        id = 'Nepal'
    elif message=="Macao" :
        id = 'Macao'
    elif message=="Сирия" :
        id = 'Syria'
    elif message=="Мозамбик" :
        id = 'Mozambique'
    elif message=="Эритрея" :
        id = 'Eritrea'
    elif message=="Святой мартин" :
        id = 'Saint Martin'
    elif message=="Монголия" :
        id = 'Mongolia'
    elif message=="Малави" :
        id = 'Malawi'
    elif message=="Чад" :
        id = 'Chad'
    elif message=="Eswatini" :
        id = 'Eswatini'
    elif message=="Зимбабве" :
        id = 'Zimbabwe'
    elif message=="Ангола" :
        id = 'Angola'
    elif message=="Ботсвана" :
        id = 'Botswana'
    elif message=="Лаос" :
        id = 'Laos'
    elif message=="Белиз" :
        id = 'Belize'
    elif message=="Фиджи" :
        id = 'Fiji'
    elif message=="Доминика" :
        id = 'Dominica'
    elif message=="Намибия" :
        id = 'Namibia'
    elif message=="Гренада" :
        id = 'Grenada'
    elif message=="Санкт-Люсия" :
        id = 'Saint Lucia'
    elif message=="Бурунди" :
        id = 'Burundi'
    elif message=="Гренландия" :
        id = 'Greenland'
    elif message=="Монсеррат" :
        id = 'Montserrat'
    elif message=="Сейшельские острова" :
        id = 'Seychelles'
    elif message=="Никарагуа" :
        id = 'Nicaragua'
    elif message=="Гамбия" :
        id = 'Gambia'
    elif message=="Суринам" :
        id = 'Suriname'
    elif message=="Ватикан" :
        id = 'Vatican City'
    elif message=="Мавритания" :
        id = 'Mauritania'
    elif message=="Бутан" :
        id = 'Bhutan'
    elif message=="Западная Сахара" :
        id = 'Western Sahara'
    elif message=="Ангилья" :
        id = 'Anguilla'
    elif message=="Йемен" :
        id = 'Yemen'
    else :
        message_cb(bot, event)
    bot.send_text(chat_id=event.data['chat']['chatId'],
                  text=f"Данные по стране: {event.text}\n"
                       f"Заболевших: {cases.loc[id, 'Total Cases']} ({cases.loc[id, 'New Cases']})\n"
                       f"Смертей: {cases.loc[id, 'Total Deaths']}({cases.loc[id, 'New Deaths']})\n"
                       f"Выздоровело: {cases.loc[id, 'Total Recovered']}\n"
                       f"Протестировано: {cases.loc[id, 'Total Tests']}", )


bot.dispatcher.add_handler(MessageHandler(callback=message_stats))
bot.dispatcher.add_handler(MessageHandler(filters=Filter.regexp("/start*"), callback=message_cb))
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons_answer_cb))

bot.start_polling()
bot.idle()
