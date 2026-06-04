import sqlite3

db = sqlite3.connect("wasteland.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    user_id INTEGER PRIMARY KEY,

    level INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,

    health INTEGER DEFAULT 100,
    armor INTEGER DEFAULT 0,
    stamina INTEGER DEFAULT 100,

    weapon_level INTEGER DEFAULT 1,
    ammo INTEGER DEFAULT 9,

    cnr_dollars INTEGER DEFAULT 0,
    bonds INTEGER DEFAULT 0,
    atomic_caps INTEGER DEFAULT 0,

    chips INTEGER DEFAULT 0,
    processors INTEGER DEFAULT 0,
    modules INTEGER DEFAULT 0,
    cores INTEGER DEFAULT 0,

    grenades INTEGER DEFAULT 3,
    syringes INTEGER DEFAULT 3
)
""")

db.commit()


def create_player(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO players (user_id) VALUES (?)",
        (user_id,)
    )
    db.commit()


def get_player(user_id):
    cursor.execute(
        "SELECT * FROM players WHERE user_id=?",
        (user_id,)
    )
    return cursor.fetchone()


def add_xp(user_id, amount):
    cursor.execute(
        "UPDATE players SET xp=xp+? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def set_xp(user_id, xp):
    cursor.execute(
        "UPDATE players SET xp=? WHERE user_id=?",
        (xp, user_id)
    )
    db.commit()


def set_level(user_id, level):
    cursor.execute(
        "UPDATE players SET level=? WHERE user_id=?",
        (level, user_id)
    )
    db.commit()


def add_money(user_id, amount):
    cursor.execute(
        "UPDATE players SET cnr_dollars=cnr_dollars+? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def remove_money(user_id, amount):
    cursor.execute(
        "UPDATE players SET cnr_dollars=cnr_dollars-? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def add_chips(user_id, amount):
    cursor.execute(
        "UPDATE players SET chips=chips+? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def remove_chips(user_id, amount):
    cursor.execute(
        "UPDATE players SET chips=chips-? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def add_processors(user_id, amount):
    cursor.execute(
        "UPDATE players SET processors=processors+? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def remove_processors(user_id, amount):
    cursor.execute(
        "UPDATE players SET processors=processors-? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def add_modules(user_id, amount):
    cursor.execute(
        "UPDATE players SET modules=modules+? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def remove_modules(user_id, amount):
    cursor.execute(
        "UPDATE players SET modules=modules-? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def add_cores(user_id, amount):
    cursor.execute(
        "UPDATE players SET cores=cores+? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def remove_cores(user_id, amount):
    cursor.execute(
        "UPDATE players SET cores=cores-? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()