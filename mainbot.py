from telegram.ext import Application
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import ReplyKeyboardMarkup
# from telegram import ReplyKeyboardRemove
import logging


async def edit_data(update, context, command):
    global DATA
    if command == 'registraciya':
        DATA[str(update.message.chat.id)] = ['registraciya', [[], 'gg']]
    return context


async def start(update, context):
    if str(update.message.chat.id) not in DATA:
        await update.message.reply_text('Добро пожаловать в UC SHOP!\n'
                                        'Для продолжения нажмите "Зарегестрироваться"',
                                        reply_markup=markup[0])
        await edit_data(update, context, 'registraciya')
    else:
        n = 0
        if 'registraciya' in DATA[str(update.message.chat.id)][0]:
            n = 0
        elif 'main_menu' in DATA[str(update.message.chat.id)][0]:
            n = 1
        await update.message.reply_text("Бот уже запущен! Используйте команды для пользования!", reply_markup=markup[n])
    return context


async def register(update, context):
    global DATA
    user_id = str(update.message.chat.id)

    if update.message.text == '⚙️ Регистрация ⚙️' and DATA[user_id][0] == 'registraciya':
        DATA[user_id][0] = 'registraciya_kode'
        skip = InlineKeyboardMarkup([[InlineKeyboardButton("пропустить", callback_data='пропустить')]])
        await update.message.reply_text('⚙️ Введите реферальный код или нажмите "пропустить" ⚙️', reply_markup=skip)

    elif DATA[user_id][0] == 'registraciya_kode':
        if update.message.text in DATA:
            DATA[user_id][1][1] = update.message.text
            DATA[user_id][0] = 'main_menu'
            await update.message.reply_text("⚙️ Регистрация завершена! ⚙️", reply_markup=markup[1])
        else:
            await update.message.reply_text('⚙️ Такого реферального кода не существует! ⚙️', )
            skip = InlineKeyboardMarkup([[InlineKeyboardButton("пропустить", callback_data='пропустить')]])
            await update.message.reply_text('⚙️ Введите реферальный код или нажмите "пропустить" ⚙️', reply_markup=skip)
    elif DATA[user_id][0] == 'registraciya_gg':
        DATA[user_id][1][1] = '810302703'
        DATA[user_id][0] = 'main_menu'
        await update.message.reply_text("⚙️ Регистрация завершена! ⚙️", reply_markup=markup[1])
    return context


async def register_buttons(update, context, command):
    global DATA
    query = update.callback_query
    user_id = str(update.callback_query.from_user.id)

    if command == 'пропустить':
        DATA[user_id][0] = 'registraciya_gg'
        await query.edit_message_text("Для завершения регистрации нажмите на [⚙️ Регистрация ⚙️]")

    return context


async def main_menu(update, context):
    global DATA
    user_id = str(update.message.chat.id)
    message = update.message.text
    if message == '🛒 Купить UC':
        DATA[user_id][0] = 'main_menu_ucshop_1'
        await ucshop(update, context, 'uc_1')
    return context


async def ucshop(update, context, command):
    ucshop_1 = [
        [InlineKeyboardButton("60 + 0 UC  —  9̶5̶ ̶₽̶   88 ₽", callback_data='60UC')],
        [InlineKeyboardButton("300 + 25 UC  —  4̶7̶5̶ ̶₽̶   423 ₽", callback_data='325UC')],
        [InlineKeyboardButton("600 + 60 UC  —  9̶5̶0̶ ̶₽̶   845 ₽", callback_data='660UC')],
        [InlineKeyboardButton("1500 + 300 UC  —  2̶3̶7̶5̶ ̶₽̶   2098 ₽", callback_data='1800UC')],
        [InlineKeyboardButton("3000 + 825 UC  —  4̶7̶5̶0̶ ̶₽̶   4247 ₽", callback_data='3825UC')],
        [InlineKeyboardButton("Корзина", callback_data='Корзина'),
         InlineKeyboardButton(">>", callback_data='>>')]
    ]
    ucshop_1 = InlineKeyboardMarkup(ucshop_1)
    if command == 'uc_1':
        await update.message.reply_text("⚙️ UCSHOP ⚙️", reply_markup=ucshop_1)
    return context


async def main_menu_buttons(update, context, command):
    global DATA
    query = update.callback_query
    user_id = str(update.callback_query.from_user.id)

    ucshop_1 = [
        [InlineKeyboardButton("60 + 0 UC  —  9̶5̶ ̶₽̶   88 ₽", callback_data='60UC')],
        [InlineKeyboardButton("300 + 25 UC  —  4̶7̶5̶ ̶₽̶   423 ₽", callback_data='325UC')],
        [InlineKeyboardButton("600 + 60 UC  —  9̶5̶0̶ ̶₽̶   845 ₽", callback_data='660UC')],
        [InlineKeyboardButton("1500 + 300 UC  —  2̶3̶7̶5̶ ̶₽̶   2098 ₽", callback_data='1800UC')],
        [InlineKeyboardButton("3000 + 825 UC  —  4̶7̶5̶0̶ ̶₽̶   4247 ₽", callback_data='3825UC')],
        [InlineKeyboardButton("Корзина", callback_data='Корзина'),
         InlineKeyboardButton(">>", callback_data='>>')]
    ]
    ucshop_1 = InlineKeyboardMarkup(ucshop_1)
    ucshop_2 = [
        [InlineKeyboardButton("6000 + 2100 UC  —  9̶5̶0̶0̶ ̶₽̶   8493 ₽", callback_data='8100UC')],
        [InlineKeyboardButton("15000 + 1200 UC  —  2̶3̶7̶5̶0̶ ̶₽̶   16883 ₽", callback_data='16200UC')],
        [InlineKeyboardButton("22000 + 2300 UC  —  3̶4̶8̶5̶0̶ ̶₽̶   25324 ₽", callback_data='24300UC')],
        [InlineKeyboardButton("30000 + 2400 UC  —  4̶7̶5̶0̶0̶ ̶₽̶   34180 ₽", callback_data='32400UC')],
        [InlineKeyboardButton("37000 + 3500 UC  —  5̶8̶6̶0̶0̶ ̶₽̶   42989 ₽", callback_data='40500UC')],
        [InlineKeyboardButton("Корзина", callback_data='Корзина'),
         InlineKeyboardButton("<<", callback_data='<<')]
    ]
    ucshop_2 = InlineKeyboardMarkup(ucshop_2)

    if 'ucshop' in DATA[user_id][0]:
        if command == '>>':
            await query.edit_message_text("⚙️ UCSHOP ⚙️", reply_markup=ucshop_2)
        elif command == '<<':
            await query.edit_message_text("⚙️ UCSHOP ⚙️", reply_markup=ucshop_1)
    return context


async def check_command(update, context):
    user_id = str(update.message.chat.id)

    if 'registraciya' in DATA[user_id][0]:
        await register(update, context)
    if 'main_menu' in DATA[user_id][0]:
        await main_menu(update, context)


async def button(update, context):
    query = update.callback_query
    await query.answer()
    answer = str(query.data)
    user_id = str(update.callback_query.from_user.id)

    if DATA[user_id][0] == 'registraciya_kode':
        await register_buttons(update, context, answer)

    if 'main_menu' in DATA[user_id][0]:
        await main_menu_buttons(update, context, answer)

    return context


def main():
    application = Application.builder().token('7377220330:AAHTt7-meneFMEVV2OL3kcYgKgjyovMmR-M').build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_command))

    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()


# DATA = {user_id: ['kode', [['1', '2' - referals], 'more info']]}
DATA = {}
with open('data.txt', encoding='utf-8') as DATA_READ:
    DATA_READ = DATA_READ.readlines()
    for el in DATA_READ:
        el = el.split('/')
        DATA[el[0]] = [el[1], [el[2][:-1].split(';')[0].split(':'), el[2][:-1].split(';')[1]]]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

reply_keyboard_reg = [['⚙️ Регистрация ⚙️']]
reply_keyboard_main = [['🛒 Купить UC', '🎁 UC бесплатно'], ['🗂 Профиль', '📖 Информация']]
markup = [ReplyKeyboardMarkup(reply_keyboard_reg, resize_keyboard=True, one_time_keyboard=False),
          ReplyKeyboardMarkup(reply_keyboard_main, resize_keyboard=True, one_time_keyboard=False)]

if __name__ == '__main__':
    main()

with open('data.txt', 'w') as data:
    s = []
    for el in DATA:
        s.append(f'{el}/' + f'{DATA[el][0]}/' + f'{":".join(DATA[el][1][0])}' + ';' + f'{DATA[el][1][1]}' + '\n')
    for elem in s:
        data.write(elem)
    print('success exit')
