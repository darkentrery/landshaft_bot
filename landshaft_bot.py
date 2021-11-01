#import config
import logging
import asyncio
import sqlite3
import io
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from client_base import Table

#from config import *
#from messages import *
API_TOKEN = ""
database = "./clients_base.db"

inna_id = ''
my_id =  ''
my_id = inna_id

#@landshaft_profi_bot

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()

bot = Bot(token=API_TOKEN)#, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot, loop=loop)

PRICE = types.LabeledPrice(label='Настоящая Машина Времени', amount=10000)

#cb = CallbackData("id", "action")

inline_btn_V_0 = types.InlineKeyboardButton('Вводный урок пройден', callback_data='buttonV_0')
inline_kb_V_0 = types.InlineKeyboardMarkup().add(inline_btn_V_0)
inline_btn_V_0_1 = types.InlineKeyboardButton('Анкета заполнена', callback_data='buttonV_0_1')
inline_kb_V_0_1 = types.InlineKeyboardMarkup().add(inline_btn_V_0_1)
inline_btn_V_1 = types.InlineKeyboardButton('Заданние №1 пройдено', callback_data='buttonV_1')
inline_kb_V_1 = types.InlineKeyboardMarkup().add(inline_btn_V_1)
inline_btn_V_2 = types.InlineKeyboardButton('Заданние №2 пройдено', callback_data='buttonV_2')
inline_kb_V_2 = types.InlineKeyboardMarkup().add(inline_btn_V_2)
inline_btn_V_3 = types.InlineKeyboardButton('Заданние №3 пройдено', callback_data='buttonV_3')
inline_kb_V_3 = types.InlineKeyboardMarkup().add(inline_btn_V_3)
inline_btn_V_4 = types.InlineKeyboardButton('Заданние №4 пройдено', callback_data='buttonV_4')
inline_kb_V_4 = types.InlineKeyboardMarkup().add(inline_btn_V_4)
inline_btn_V_5 = types.InlineKeyboardButton('Заданние №5 пройдено', callback_data='buttonV_5')
inline_kb_V_5 = types.InlineKeyboardMarkup().add(inline_btn_V_5)

inline_btn_1_1 = types.InlineKeyboardButton('Посмотрел', callback_data='button1_1')
inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1_1)

inline_btn_2_1 = types.InlineKeyboardButton('Да', callback_data='button2_1')
inline_btn_2_2 = types.InlineKeyboardButton('Нет', callback_data='button2_2')
inline_kb2 = types.InlineKeyboardMarkup().add(inline_btn_2_1, inline_btn_2_2)

inline_btn_3_1 = types.InlineKeyboardButton('Отослать форму регистрации', callback_data='button3_1')
inline_kb3 = types.InlineKeyboardMarkup().add(inline_btn_3_1)

inline_btn_7_1 = types.InlineKeyboardButton('Да', callback_data='button7_1')
inline_btn_7_2 = types.InlineKeyboardButton('Нет', callback_data='button7_2')
inline_kb7 = types.InlineKeyboardMarkup().add(inline_btn_7_1, inline_btn_7_2)

inline_btn_8_1 = types.InlineKeyboardButton('Тариф №1', callback_data='button8_1')
inline_btn_8_2 = types.InlineKeyboardButton('Тариф №2', callback_data='button8_2')
inline_btn_8_3 = types.InlineKeyboardButton('Тариф №3', callback_data='button8_3')
inline_kb8 = types.InlineKeyboardMarkup().add(inline_btn_8_1, inline_btn_8_2, inline_btn_8_3)

inline_kb9 = types.InlineKeyboardMarkup()
btn_cancel = types.InlineKeyboardButton('Отмена', callback_data='button9_' + str(5))
for i in range(5):
    btn_9 = types.InlineKeyboardButton('Ответить на ДЗ №' + str(i+1), callback_data='button9_' + str(i))
    inline_kb9.add(btn_9)
inline_kb9.add(btn_cancel)

doc_for_lesson_0_1 = "./doc_for_lesson_0_1.pdf"
doc_for_lesson_0_2 = "./doc_for_lesson_0_2.pdf"

doc_for_lesson_2_1 = "./doc_for_lesson_2_1.pdf"
doc_for_lesson_2_2 = "./doc_for_lesson_2_2.pdf"
doc_for_lesson_2_3 = "./doc_for_lesson_2_3.pdf"

doc_for_lesson_3_1 = "./doc_for_lesson_3_1.jpg"
doc_for_lesson_3_2 = "./doc_for_lesson_3_2.jpg"

doc_for_lesson_4_1 = "./doc_for_lesson_4_1.mp4"

doc_for_lesson_5_1 = "./doc_for_lesson_5_1.jpg"

aa = 1
a = 1
b = 2
c = 3

Table(database).read_all()

@dp.message_handler(commands=['terms'])
async def process_terms_command(message: types.Message):
    await message.reply(MESSAGES['terms'], reply=False)

@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

#Функция старта бота
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id == my_id:
        await message.answer("Введите имя ученика, которому хотите ответить.")
    else:
        if Table(database).find_user(user_id) == 0:
            Table(database).connection(user_id)
        Table(database).write_password_0(user_id)
        await message.answer("Пожалуйста введите полученный пароль")

        #await message.answer("Занятие 1 (Знакомство с преподавателем / инструменты для курса / "
        #                     "Программа курса / бонусы тем кто сделает все задания - разбор итоговой схемы "
        #                     "Бесплатная консультация в подарок / задать вопрос преподавателю) + "
        #                     "текстовое сообщение как просмотрите напишите в чате «Посмотрел» ", reply_markup=inline_kb1)

#Обработчик нажатия кнопки после первого ролика
@dp.callback_query_handler(lambda c: c.data == 'button1_1')
async def process_callback_button1_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Опрос: заинтересовала программа курса?', reply_markup=inline_kb2)

    """if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(callback_query.from_user.id, MESSAGES['pre_buy_demo_alert'])
        await bot.send_invoice(
            callback_query.from_user.id,
            title=MESSAGES['tm_title'],
            description=MESSAGES['tm_description'],
            provider_token=PAYMENTS_PROVIDER_TOKEN,
            currency='rub',
            photo_url=TIME_MACHINE_IMAGE_URL,
            photo_height=512,  # !=0/None, иначе изображение не покажется
            photo_width=512,
            photo_size=512,
            is_flexible=False,  # True если конечная цена зависит от способа доставки
            prices=[PRICE],
            start_parameter='time-machine-example',
            payload='some-invoice-payload-for-our-internal-use'
        )"""

#Обработчик нажатия кнопки в случае если курс заинтересовал
@dp.callback_query_handler(lambda c: c.data == 'button2_1')
async def process_callback_button2_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    #await bot.send_message(callback_query.from_user.id, 'Заполните форму регистрации. Введите фамилию и имя в формате Иванов Иван')
    #Table(database).write_name_0(callback_query.from_user.id)

#Обрабатываем события ввода сообщения. Происходит проверка готовности к записи конкретной ячейки базы данных
@dp.message_handler()
async def write_data(message: types.Message):
    if message.from_user.id != my_id:
        if Table(database).write_password(message.from_user.id, message.text) == True:
            await message.answer('Заполните форму регистрации. Введите фамилию и имя в формате Иванов Иван')
            Table(database).write_name_0(message.from_user.id)
        elif Table(database).write_password(message.from_user.id, message.text) == 2:
            await message.answer("Вы введи неверный пароль. Попробуйте пожалуйста снова.")
        elif Table(database).write_name(message.from_user.id, message.text) == True:
            await message.answer("Введите номер телефона")
        elif Table(database).write_name(message.from_user.id, message.text) == 2:
            await message.answer("Вы выбрали неверный формат имени. Попробуйте пожалуйста снова.")
        elif Table(database).write_phone(message.from_user.id, message.text) == True:
            await message.answer("Введите Instagram")
        elif Table(database).write_phone(message.from_user.id, message.text) == 2:
            await message.answer("Вы выбрали неверный формат номера телефона. Попробуйте пожалуйста снова.")
        elif Table(database).write_instagram(message.from_user.id, message.text) == True:
            #await message.answer("Занятие 0 (Знакомство с преподавателем / инструменты для курса / "
            #                     "Программа курса / бонусы тем кто сделает все задания - разбор итоговой схемы "
            #                     "Бесплатная консультация в подарок / задать вопрос преподавателю) + "
            #                     "текстовое сообщение как просмотрите напишите в чате «Посмотрел» ",
            #                     reply_markup=inline_kb_V_0)
            await message.answer("https://youtu.be/O7kTkHG3HZk")
            await bot.send_document(message.from_user.id, open(doc_for_lesson_0_1, "rb"))
            await bot.send_document(message.from_user.id, open(doc_for_lesson_0_2, "rb"))
            await message.answer('Дорогие участники курса!\n\n'
                                                          ' Для вашего удобства к списку канцелярии прикрепляется '
                                                          'подборка с ссылками на Яндекс.Маркет. Посмотрев примеры из '
                                                          'списка рекомендуемых канцелярских товаров вы сможете выбрать '
                                                          'как вам удобнее - купить в своем городе или заказать с '
                                                          'доставкой через интернет.')
            await message.answer('https://docs.google.com/spreadsheets/d/1vs7E4NSppKc8VaDbOA9rJTTNhbvG7BfBEHLCNklKQMU/edit?usp=sharing',
                                    reply_markup=inline_kb_V_0)
        elif Table(database).write_learn(message.from_user.id, message.text) == True:
            await message.answer('Спасибо за Вашу обратную связь')

        for i in range(5):
            if Table(database).write_after(message.from_user.id, i + 1, message.text) == True:
                await message.answer('Отправьте домашнее задание в формате рисунка или документа.'
                                     ' После выполнения домашнего задания вы сможете продолжить знакомство с курсом.')

    #Обработчик сообщений от учителя
    else:
        names = Table(database).find_name(message.text)
        if len(names) != 0:
            inline_kb10 = types.InlineKeyboardMarkup()
            for i in range(len(names)):
                user_id = Table(database).read_id(names[i])
                btn = types.InlineKeyboardButton(str(names[i]), callback_data='btn' + str(user_id))
                inline_kb10.add(btn)
            await bot.send_message(my_id, "Ответьте", reply_markup=inline_kb10)
            for i in range(len(names)):
                user_id = Table(database).read_id(names[i])
                btn = 'btn' + str(user_id)
                @dp.callback_query_handler(lambda c, btn=btn: c.data == btn)
                async def process_callback_btn(callback_query: types.CallbackQuery):
                    global user_id_d
                    user_id_d = user_id
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(my_id, "Ответьте ученику на задание", reply_markup=inline_kb9)

            for h in range(5):
                @dp.callback_query_handler(lambda c, h=h: c.data == 'button9_' + str(h))
                async def process_callback_btn9(callback_query: types.CallbackQuery):
                    for f in range(5):
                        if callback_query.data == 'button9_' + str(f):
                            if Table(database).read_h_w(user_id_d, f + 1) != 'True' and Table(database).read_h_w(user_id_d, f + 1) != 'False':
                                Table(database).write_h_w_a(user_id_d, f + 1)
                                await bot.answer_callback_query(callback_query.id)
                                await bot.send_message(my_id, "Напишите ваш ответ или вставьте файл")
                            else:
                                await bot.answer_callback_query(callback_query.id)
                                await bot.send_message(my_id, "Ученик еще не выполнил это домашнее задание")
                                await bot.send_message(my_id, "Введите имя ученика, которому хотите ответить.")

            Table(database).read_all()

        user_ids = Table(database).read_ids()

        if user_ids != None:
            @dp.callback_query_handler(lambda c: c.data == 'button9_' + str(5))
            async def process_callback_btn_cancel(callback_query: types.CallbackQuery):
                for id in range(len(user_ids)):
                    for y in range(5):
                        if Table(database).read_h_w_a(user_ids[id], y + 1) == 'True':
                            Table(database).write_h_w_a(user_ids[id], y + 1)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(my_id, "Введите имя ученика, которому хотите ответить.")

            for id in range(len(user_ids)):
                for ii in range(5):
                    if Table(database).read_h_w_a(user_ids[id], ii + 1) == 'True':
                        Table(database).write_h_w_a(user_ids[id], ii + 1)
                        message_id = Table(database).read_h_w(user_ids[id], ii + 1)
                        await bot.send_message(user_ids[id], str(message.text), reply_to_message_id=message_id)
                        await message.answer("Введите имя ученика, которому хотите ответить.")


            Table(database).read_all()


#Обработчик отправленных домашних заданий
@dp.message_handler(content_types=['document', 'photo'])
async def write_h_w(message: types.Message):
    if message.document is not None:
        document = message.document
        typ = "doc"
    else:
        document = message.photo[1]
        typ = "photo"
    file_id = await bot.get_file(document.file_id)
    doc = await bot.download_file(file_id.file_path)

    # Обработчик сообщений от ученика
    if message.from_user.id != my_id:
        for i in range(5):
            if Table(database).write_h_w(message.from_user.id, i + 1, str(message.message_id)) == True:
                name = Table(database).read_name(message.from_user.id)
                if typ == "doc":
                    await bot.send_document(my_id, (str(document.file_name), doc))
                else:
                    await bot.send_photo(my_id, doc)
                await bot.send_message(my_id, "Проверьте домашнее задание по уроку №" + str(i + 1) + " от " + name)
                await message.answer('Спасибо за обратную связь. Ваше домашнее задание получено. '
                                     'Обычно проверка занимает не более суток. '
                                     'Пока преподаватель производит проверку и готовит новое задание, вы можете передохнуть.')
                if i == 0:
                    await message.answer('https://youtu.be/HwmyoSTxuS8')
                    await message.answer('https://www.youtube.com/watch?v=D7CnJ57oXa0&ab_channel=%D0%98%D0%BD%D0%BD%D0%B0%D0%A1%D0%B0%D0%B4%D1%8B%D0%BA%D0%BE%D0%B2%D0%B0')
                    await bot.send_document(message.from_user.id, open(doc_for_lesson_2_1, "rb"))
                    await bot.send_document(message.from_user.id, open(doc_for_lesson_2_2, "rb"))
                    await bot.send_document(message.from_user.id, open(doc_for_lesson_2_3, "rb"), reply_markup=inline_kb_V_2)
                elif i == 1:
                    await message.answer('Урок 3\n\n В этом уроке рассмотрим правила оформления дорожек и площадок под зону'
                                         ' отдыха. Урок состоит из двух частей. Досмотрите их до конца и приступайте '
                                         'к выполнению домашнего задания. Пример результата домашнего задания во вложении.\n\n'
                                         'https://youtu.be/NNLcUWxk0Lk')
                    await message.answer('https://youtu.be/pkuUdEyAX1M')
                    await bot.send_document(message.from_user.id, open(doc_for_lesson_3_1, "rb"))
                    await bot.send_document(message.from_user.id, open(doc_for_lesson_3_2, "rb"), reply_markup=inline_kb_V_3)
                elif i == 2:
                    await message.answer('Урок 4\n\n На прошом уроке мы наметили площадку и тропинки к зоне отдыха. '
                                         'Давайте теперь определимся с материалами и как их сочетать.\n\n'
                                         'https://www.youtube.com/watch?v=DaFYI9cBFFw&ab_channel=%D0%98%D0%BD%D0%BD%D0%B0%D0%A1%D0%B0%D0%B4%D1%8B%D0%BA%D0%BE%D0%B2%D0%B0')
                    await message.answer('Пример того, как смотрятся малые архитектрные формы в сочетании с архитектурой')
                    await bot.send_video(message.from_user.id, open(doc_for_lesson_4_1, "rb"))
                    await message.answer('Подборка с декором\n\n'
                                         ' https://docs.google.com/spreadsheets/d/1EMVzYupsnFX8Nyvn1EAl8fhq9VbYXslFk8P04IT2cOQ/edit?usp=sharing')
                    await message.answer('Материалы для сада\n\n '
                                         'https://docs.google.com/spreadsheets/d/1FE96HJK7eBBXZFTiHM8grModNHorA4lwO8ReQdOHJkE/edit?usp=sharing',
                                         reply_markup=inline_kb_V_4)
                elif i == 3:
                    await message.answer('Урок 5\n\n Посмотрите внимательно финальный урок, чтобы понять принцип подбора'
                                         ' растений на участке. https://youtu.be/aJu-dxDWVT4')
                    await message.answer('Пример домашнего задания')
                    await bot.send_document(message.from_user.id, open(doc_for_lesson_5_1, "rb"), reply_markup=inline_kb_V_5)
                elif i == 4:
                    await message.answer('Спасибо за выбор нашего курса! Ждем Вас на других обучающих программах!')



    """elif Table(database).write_h_w_5(message.from_user.id, str(message.message_id)) == True:
        name = Table(database).read_name(message.from_user.id)
        if typ == "doc":
            await bot.send_document(my_id, (str(document.file_name), doc))
        else:
            await bot.send_photo(my_id, doc)
        await bot.send_message(my_id, "Проверьте домашнее задание по уроку №5 от " + name)
        await message.answer('Спасибо за обратную связь. Ваше домашнее задание получено. '
                             'Обычно проверка занимает не более суток. '
                             'Пока преподаватель производит проверку, вы можете завершить ознакомительную часть курса.')
        await message.answer('Видео благодарность за прохождение курса, резюме усвоенной программы на бесплатной части.'
                             ' Анонс того, что можно сделать ещё (разработать цветники). Результат разбора ДЗ в течении'
                             ' 24 часов. Отправьте ДЗ. Для получения ДЗ напишите в чате "ДЗ"')
        await message.answer("Опрос: Желаете продолжить обучение и украсить свою зону отдыха красивыми цветниками?",
                             reply_markup=inline_kb7)"""
    Table(database).read_all()

    # Обработчик сообщений от учителя
    if message.from_user.id == my_id:
        user_ids = Table(database).read_ids()
        if user_ids != None:
            for id in range(len(user_ids)):
                for ii in range(5):
                    if Table(database).read_h_w_a(user_ids[id], ii + 1) == 'True':
                        Table(database).write_h_w_a(user_ids[id], ii + 1)
                        message_id = Table(database).read_h_w(user_ids[id], ii + 1)
                        if typ == "doc":
                            await bot.send_document(user_ids[id], (str(document.file_name), doc),
                                                    reply_to_message_id=message_id)
                        else:
                            await bot.send_photo(user_ids[id], doc, reply_to_message_id=message_id)
                        await message.answer("Введите имя ученика, которому хотите ответить.")


#Обработчик нажатия кнопки в случае если курс не заинтересовал
@dp.callback_query_handler(lambda c: c.data == 'button2_2')
async def process_callback_button2_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Вы какашки')

#Обработчик нажатия кнопки после нулевого ролика
@dp.callback_query_handler(lambda c: c.data == 'buttonV_0')
async def process_callback_buttonV_0(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Пожалуста перейдите по ссылке для заполнения анкеты')
    await bot.send_message(callback_query.from_user.id, ' https://forms.gle/L9MScmnsUCQbofZa8', reply_markup=inline_kb_V_0_1)

#Обработчик нажатия кнопки после регистрации в Google форме
@dp.callback_query_handler(lambda c: c.data == 'buttonV_0_1')
async def process_callback_buttonV_0_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Этот урок состоит из двух частей.'
                                                        ' Сначала посмотрите обе части, а потом приступайте к выполнению домашнего задания.\n\n'
                                                        'Для того, чтобы определится с наполнением зоны отдыха предлагаю '
                                                        'пойти по творческому методу. Конечно в рамках курса мы разберём '
                                                        'аспекты функционального наполнения, чтобы вы разобрались с '
                                                        'типами малых архитектурных форм, которые применяются в зонах отдыха.\n\n'
                                                        'Очень хочется дать вам больше, чем то о чем пишут в интернете'
                                                        ' и книгах. Желаю вам прочувствовать как сделать из уголка для'
                                                        ' отдыха место силы. Чтобы это место соответствовало вашим'
                                                        ' внутренним потребностям души.\n\n'
                                                        'Видео лекция урока 1. Первая часть\n\n'
                                                        ' https://youtu.be/5t3aJQWQpOg \n\n')
    await bot.send_message(callback_query.from_user.id, 'https://www.youtube.com/watch?v=Yg-W5rAQ4AY\n\n'
                                                        'Таблица с элементами для вашей зоны отдыха. Список будет пополнятся\n\n'
                                                        'https://docs.google.com/spreadsheets/d/1eCLu3LSMyODSLojTas8EH84q-I05Pb_3lCHxDpl7i30/edit?usp=sharing')
    await bot.send_message(callback_query.from_user.id, 'https://www.youtube.com/watch?v=n3GpI2HjE7I&ab_channel=GARDENBOOM-%D0%9B%D0%B0%D0%BD%D0%B4%D1%88%D0%B0%D1%84%D1%82%D0%BD%D1%8B%D0%B9%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%D0%B8%D0%BE%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5', reply_markup=inline_kb_V_1)

#Обработчик нажатия кнопки после задания №1
@dp.callback_query_handler(lambda c: c.data == 'buttonV_1')
async def process_callback_buttonV_1(callback_query: types.CallbackQuery):
    Table(database).write_after_0(callback_query.from_user.id, 1)
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Пожалуйста ответьте на три вопроса:\n\n'
                                                        ' Вопрос 1: Отдыхом в какой зоне отдыха выходите гордится?\n'
                                                        ' Вопрос 2: Отдыхом с кем в этой зоне отдыха вы хотите гордится?\n'
                                                        ' Вопрос 3: Каким окружением зоны отдыха вы хотите гордится?')

#Обработчик нажатия кнопки после задания №2
@dp.callback_query_handler(lambda c: c.data == 'buttonV_2')
async def process_callback_buttonV_2(callback_query: types.CallbackQuery):
    Table(database).write_after_0(callback_query.from_user.id, 2)
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Поделитесь обратной связью после пройденного урока. '
                                                        'Что узнали для себя нового?')

#Обработчик нажатия кнопки после задания №3
@dp.callback_query_handler(lambda c: c.data == 'buttonV_3')
async def process_callback_buttonV_3(callback_query: types.CallbackQuery):
    Table(database).write_after_0(callback_query.from_user.id, 3)
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Оцените от 1 до 10 на сколько вам понравился урок. Нам важна ваша обратная связь.')

#Обработчик нажатия кнопки после задания №4
@dp.callback_query_handler(lambda c: c.data == 'buttonV_4')
async def process_callback_buttonV_4(callback_query: types.CallbackQuery):
    Table(database).write_after_0(callback_query.from_user.id, 4)
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Поделитесь своими впечатлениями. Что нового вы узнали из урока? '
                                                        'Был ли урок вам полезен?')

#Обработчик нажатия кнопки после задания №5
@dp.callback_query_handler(lambda c: c.data == 'buttonV_5')
async def process_callback_buttonV_5(callback_query: types.CallbackQuery):
    Table(database).write_after_0(callback_query.from_user.id, 5)
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Поделитесь своими впечатлениями. Что нового вы узнали из урока? '
                                                        'Был ли урок вам полезен?')

#Обработчик нажатия кнопки готовности пройти обучение
@dp.callback_query_handler(lambda c: c.data == 'button7_1')
async def process_callback_button7_1(callback_query: types.CallbackQuery):
    Table(database).write_learn(callback_query.from_user.id, "yes")
    Table(database).write_tariff_0(callback_query.from_user.id)
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Видео приглашение на курс. Скидка за скорость + '
                                                        'Описание тарифов. Какой тариф желаете приобрести ?', reply_markup=inline_kb8)
    #если не отвечают еще нужно каждые 24 часа напоминать

#Обработчик нажатия кнопки не готовности пройти обучение
@dp.callback_query_handler(lambda c: c.data == 'button7_2')
async def process_callback_button7_2(callback_query: types.CallbackQuery):
    Table(database).write_learn_0(callback_query.from_user.id)
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Опрос: почему не решились пройти обучение?')

#Обработчик нажатия кнопки готовности пройти обучение
@dp.callback_query_handler(lambda c: c.data == 'button8_1')
async def process_callback_button8_1(callback_query: types.CallbackQuery):
    Table(database).write_tariff(callback_query.from_user.id, "1")
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Спасибо, что выбрали наш курс!'
                                                        ' Ваш тариф №1 - это прекрасный выбор.', reply_markup=inline_kb8)

async def auto():
    while True:
        await asyncio.sleep(10)
        #await bot.send_message(my_id, text="fesz")

loop = asyncio.get_event_loop()
loop.create_task(auto())
#dp.loop.create_task(auto())
executor.start_polling(dp, skip_updates=True)
