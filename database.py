import sqlite3

db = sqlite3.connect(“wasteland.db”)
cursor = db.cursor()

cursor.execute(”””
CREATE TABLE IF NOT EXISTS players (
user_id INTEGER PRIMARY KEY,
level INTEGER DEFAULT 1,
xp INTEGER DEFAULT 0,
health INTEGER DEFAULT 100,
armor INTEGER DEFAULT 0,
stamina INTEGER DEFAULT 100,
weapon_level INTEGER DEFAULT 1,
cnr_dollars INTEGER DEFAULT 0,
bonds INTEGER DEFAULT 0,
atomic_caps INTEGER DEFAULT 0
)
“””)

db.commit()

def create_player(user_id):
cursor.execute(
“INSERT OR IGNORE INTO players (user_id) VALUES (?)”,
(user_id,)
)
db.commit()

def get_player(user_id):
cursor.execute(
“SELECT * FROM players WHERE user_id = ?”,
(user_id,)
)
return cursor.fetchone()
