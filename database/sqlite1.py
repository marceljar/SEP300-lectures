from data import users
import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
    CREATE TABLE users (
        user_id     INTEGER PRIMARY KEY,
        first_name  TEXT NOT NULL,
        last_name   TEXT NOT NULL,
        balance     NUMERIC(10,2) NOT NULL
    )
""")

for u in users:
    cursor.execute(
        f"INSERT INTO users (user_id, first_name, "
        f"last_name, balance) "
        f"VALUES ({int(u['user_id'])}, "
        f"'{u['first_name']}', '{u['last_name']}', "
        f"{float(u['balance']):.2f})"
    )

conn.commit()
conn.close()