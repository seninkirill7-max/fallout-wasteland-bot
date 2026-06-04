import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = os.getenv(“BOT_TOKEN”)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_menu():
builder = ReplyKeyboardBuilder()

builder.button(text="📊 Статистика")
builder.button(text="🎒 Инвентарь")
builder.button(text="☢ Выход в Пустоши")
builder.button(text="🏋 Тренировочный зал")
builder.button(text="🛒 Торговая лавка")
builder.button(text="🏛 Обменный бункер")
builder.adjust(1)
return builder.as_markup(resize_keyboard=True)

@dp.message(F.text == “/start”)
async def start(message: Message):
await message.answer(
“☢ ПУСТОШИ ☢\n\nДобро пожаловать в Пустоши.”,
reply_markup=main_menu()
)

@dp.message(F.text == “📊 Статистика”)
async def stats(message: Message):
await message.answer(
“📊 Статистика персонажа\n\n”
“Уровень: 1\n”
“Опыт: 0\n”
“Здоровье: 100\n”
“Броня: 0\n”
“Выносливость: 100\n”
“Уровень оружия: 1”
)

async def main():
await dp.start_polling(bot)

if name == “main”:
asyncio.run(main())
