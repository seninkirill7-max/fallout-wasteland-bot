import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database import create_player, get_player

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
create_player(message.from_user.id)

await message.answer(
    "☢ ПУСТОШИ ☢\n\nДобро пожаловать в Пустоши.",
    reply_markup=main_menu()
)

@dp.message(F.text == “📊 Статистика”)
async def stats(message: Message):
player = get_player(message.from_user.id)

await message.answer(
    f"📊 Статистика персонажа\n\n"
    f"Уровень: {player[1]}\n"
    f"Опыт: {player[2]}\n"
    f"❤️ Здоровье: {player[3]}\n"
    f"🛡 Броня: {player[4]}\n"
    f"⚡ Выносливость: {player[5]}\n"
    f"🔫 Уровень оружия: {player[6]}\n\n"
    f"💴 Доллары КНР: {player[7]}\n"
    f"🎟 Облигации: {player[8]}\n"
    f"⚛ Атомные крышки: {player[9]}"
)

@dp.message(F.text == “🎒 Инвентарь”)
async def inventory(message: Message):
await message.answer(
“🎒 Инвентарь\n\n”
“Склад ресурсов пока пуст.”
)

@dp.message(F.text == “☢ Выход в Пустоши”)
async def wasteland(message: Message):
await message.answer(
“☢ Выберите доступную локацию.\n\n”
“🪨 Окрестности Убежища (1 уровень)”
)

@dp.message(F.text == “🏋 Тренировочный зал”)
async def gym(message: Message):
await message.answer(
“🏋 Для входа необходимы Облигации.”
)

@dp.message(F.text == “🛒 Торговая лавка”)
async def shop(message: Message):
await message.answer(
“🛒 Торговая лавка пока закрыта.”
)

@dp.message(F.text == “🏛 Обменный бункер”)
async def bunker(message: Message):
await message.answer(
“🏛 Здесь можно будет обменивать Атомные крышки.”
)

async def main():
await dp.start_polling(bot)

if name == “main”:
asyncio.run(main())
