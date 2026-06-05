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
    add_processors,
    add_modules,
    add_cores,
    add_money,
    set_xp,
    set_level,
    sell_all_chips,
    sell_all_processors,
    sell_all_modules,
    sell_all_cores
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


def check_level_up(user_id):
    player = get_player(user_id)

    level = player[1]
    xp = player[2]

    while xp >= level * 100:
        xp -= level * 100
        level += 1

    set_level(user_id, level)
    set_xp(user_id, xp)


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
        f"⭐ Опыт: {player[2]}/{player[1] * 100}\n\n"
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
    user_id = message.from_user.id

    enemies = [
        "Радтаракан",
        "Кротокрыс",
        "Дикий гуль",
        "Рейдер",
        "Послушник Братства Стали"
    ]

    enemy = random.choice(enemies)

    xp_reward = random.randint(5, 15)
    money_reward = random.randint(5, 20)

    add_xp(user_id, xp_reward)
    add_money(user_id, money_reward)

    loot_text = ""

    player = get_player(user_id)
    level = player[1]

    chips = random.randint(1, 3)
    add_chips(user_id, chips)
    loot_text += f"⚙ Микросхемы: {chips}\n"

    if level >= 10 and random.randint(1, 100) <= 25:
        add_processors(user_id, 1)
        loot_text += "💾 Найден военный процессор: 1\n"

    if level >= 25 and random.randint(1, 100) <= 15:
        add_modules(user_id, 1)
        loot_text += "🔷 Найден тактический модуль: 1\n"

    if level >= 50 and random.randint(1, 100) <= 5:
        add_cores(user_id, 1)
        loot_text += "☢ Найдено ядерное ядро: 1\n"

    check_level_up(user_id)

    await message.answer(
        f"☢ Вы исследовали Пустоши\n\n"
        f"👤 Противник: {enemy}\n\n"
        f"🏆 Опыт: +{xp_reward}\n"
        f"💵 Доллары КНР: +{money_reward}\n\n"
        f"{loot_text}"
    )


@dp.message(F.text == "🏛 Обменный бункер")
async def bunker(message: Message):
    await message.answer(
        "🏛 ОБМЕННЫЙ БУНКЕР\n\n"
        "Напишите команду:\n\n"
        "⚙ продать микросхемы\n"
        "💾 продать процессоры\n"
        "🔷 продать модули\n"
        "☢ продать ядра\n\n"
        "Цены:\n"
        "⚙ 5 $\n"
        "💾 25 $\n"
        "🔷 100 $\n"
        "☢ 500 $"
    )


@dp.message(F.text.lower() == "продать микросхемы")
async def sell_chips(message: Message):
    amount, money = sell_all_chips(message.from_user.id)

    await message.answer(
        f"⚙ Продано микросхем: {amount}\n"
        f"💵 Получено: {money}$"
    )


@dp.message(F.text.lower() == "продать процессоры")
async def sell_processors(message: Message):
    amount, money = sell_all_processors(message.from_user.id)

    await message.answer(
        f"💾 Продано процессоров: {amount}\n"
        f"💵 Получено: {money}$"
    )


@dp.message(F.text.lower() == "продать модули")
async def sell_modules(message: Message):
    amount, money = sell_all_modules(message.from_user.id)

    await message.answer(
        f"🔷 Продано модулей: {amount}\n"
        f"💵 Получено: {money}$"
    )


@dp.message(F.text.lower() == "продать ядра")
async def sell_cores(message: Message):
    amount, money = sell_all_cores(message.from_user.id)

    await message.answer(
        f"☢ Продано ядер: {amount}\n"
        f"💵 Получено: {money}$"
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


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())