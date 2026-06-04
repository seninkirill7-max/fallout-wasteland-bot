import asyncio
import os
import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database import (
    create_player,
    get_player,
    add_xp,
    add_chips,
    add_money
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

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


@dp.message(F.text == "/start")
async def start(message: Message):
    create_player(message.from_user.id)

    await message.answer(
        "☢ ПУСТОШИ ☢\n\nДобро пожаловать в мир радиоактивных пустошей.",
        reply_markup=main_menu()
    )


@dp.message(F.text == "📊 Статистика")
async def stats(message: Message):
    player = get_player(message.from_user.id)

    await message.answer(
        f"📊 Статистика персонажа\n\n"
        f"🎖 Уровень: {player[1]}\n"
        f"⭐ Опыт: {player[2]}\n\n"
        f"❤️ Здоровье: {player[3]}\n"
        f"🛡 Броня: {player[4]}\n"
        f"⚡ Выносливость: {player[5]}\n\n"
        f"🔫 Уровень оружия: {player[6]}\n"
        f"🔸 Патроны: {player[7]}\n\n"
        f"💵 Доллары КНР: {player[8]}\n"
        f"🎟 Облигации: {player[9]}\n"
        f"⚛ Атомные крышки: {player[10]}"
    )


@dp.message(F.text == "🎒 Инвентарь")
async def inventory(message: Message):
    player = get_player(message.from_user.id)

    await message.answer(
        f"🎒 Инвентарь\n\n"
        f"⚙ Повреждённые микросхемы: {player[11]}\n"
        f"💾 Военные процессоры: {player[12]}\n"
        f"🔷 Тактические модули: {player[13]}\n"
        f"☢ Ядерные ядра: {player[14]}\n\n"
        f"💣 Гранаты: {player[15]}\n"
        f"💉 Шприцы: {player[16]}"
    )


@dp.message(F.text == "☢ Выход в Пустоши")
async def wasteland(message: Message):
    enemies = [
        "Радтаракан",
        "Кротокрыс",
        "Дикий гуль",
        "Рейдер",
        "Послушник Братства Стали"
    ]

    enemy = random.choice(enemies)

    xp_reward = random.randint(5, 15)
    chips_reward = random.randint(1, 3)
    money_reward = random.randint(5, 20)

    add_xp(message.from_user.id, xp_reward)
    add_chips(message.from_user.id, chips_reward)
    add_money(message.from_user.id, money_reward)

    await message.answer(
        f"☢ Вы исследовали Пустоши\n\n"
        f"👤 Встречен противник: {enemy}\n\n"
        f"🏆 Получено опыта: {xp_reward}\n"
        f"⚙ Получено микросхем: {chips_reward}\n"
        f"💵 Получено долларов КНР: {money_reward}"
    )


@dp.message(F.text == "🏋 Тренировочный зал")
async def gym(message: Message):
    await message.answer(
        "🏋 Тренировочный зал\n\n"
        "Для входа потребуются Облигации."
    )


@dp.message(F.text == "🛒 Торговая лавка")
async def shop(message: Message):
    await message.answer(
        "🛒 Торговая лавка\n\n"
        "Магазин находится в разработке."
    )


@dp.message(F.text == "🏛 Обменный бункер")
async def bunker(message: Message):
    await message.answer(
        "🏛 Обменный бункер\n\n"
        "Здесь можно будет обменивать Атомные крышки."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())