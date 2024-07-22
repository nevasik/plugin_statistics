import telebot
from telebot import types
from config import TELEGRAM_BOT_TOKEN, WHITELIST
from constants import START_MESSAGE, NOT_FOUND, NO_ACCESS
from sql_queries import (
    TOTAL_TURNOVER_AND_MARGIN,
    TURNOVER_AND_MARGIN_BY_PERIOD,
    CLAIM_STATUS_BY_EXTERNAL_ID,
    TOTAL_TURNOVER_AND_MARGIN_GENERAL
)
from database import Database

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
        self.db = Database()

    async def start(self):
        @self.bot.message_handler(commands=['start'])
        async def send_welcome(message):
            if message.from_user.id in WHITELIST:
                await self.send_command_description(message)
            else:
                self.bot.send_message(message.chat.id, NO_ACCESS)

        @self.bot.message_handler(func=lambda message: message.from_user.id in WHITELIST)
        async def handle_message(message):
            if message.text.startswith('/total_turnover_and_margin'):
                await self.total_turnover_and_margin(message)
            elif message.text.startswith('/turnover_and_margin_by_period'):
                await self.turnover_and_margin_by_period(message)
            elif message.text.startswith('/claim_status_by_external_id'):
                await self.claim_status_by_external_id(message)
            elif message.text.startswith('/total_turnover_and_margin_general'):
                await self.total_turnover_and_margin_general(message)

        self.bot.polling()

    async def send_command_description(self, message):
        keyboard = types.ReplyKeyboardMarkup(row_width=1)
        start_button = types.KeyboardButton('/start')
        keyboard.add(start_button)

        self.bot.send_message(message.chat.id, START_MESSAGE, reply_markup=keyboard)

    async def total_turnover_and_margin(self, message):
        query = TOTAL_TURNOVER_AND_MARGIN

        result = self.db.execute_query(query)
        if not result:
            response = NOT_FOUND
        else:
            response = "\n".join([f"{row[0]}: Оборот по PayIn: {row[1]}, Оборот по PayOut: {row[2]}, Маржа: {row[3]}" for row in result])

        self.bot.send_message(message.chat.id, response)

    async def turnover_and_margin_by_period(self, message):
        text = message.text.split()
        if len(text) != 3:
            self.bot.send_message(message.chat.id, "Используйте такую конструкцию: /turnover_and_margin_by_period <yyyy-mm-dd> <yyyy-mm-dd>")
            return
        start_date, end_date = text[1], text[2]
        query = TURNOVER_AND_MARGIN_BY_PERIOD

        result = self.db.execute_query(query, (start_date, end_date))

        if not result:
            response = NOT_FOUND
        else:
            response = "\n".join([f"{row[0]}: Оборот по PayIn: {row[1]}, Оборот по PayOut: {row[2]}, Маржа: {row[3]}" for row in result])

        self.bot.send_message(message.chat.id, response)

    async def claim_status_by_external_id(self, message):
        text = message.text.split()
        if len(text) != 2:
            self.bot.send_message(message.chat.id, "Используйте такую конструкцию: /claim_status_by_external_id <external_id>")
            return
        external_id = text[1]

        query = CLAIM_STATUS_BY_EXTERNAL_ID

        result = self.db.execute_query(query, (external_id,))
        if result:
            response = f"Статус: {result[0][0]}"
        else:
            response = f"Не найдено заявки с таким external_id={external_id}"

        self.bot.send_message(message.chat.id, response)

    async def total_turnover_and_margin_general(self, message):
        query = TOTAL_TURNOVER_AND_MARGIN_GENERAL

        result = self.db.execute_query(query)
        if not result:
            response = NOT_FOUND
        else:
            response = f"Общий оборот: {result[0][0]}, Общая маржа: {result[0][1]}"

        self.bot.send_message(message.chat.id, response)

    async def stop(self):
        self.db.close()
