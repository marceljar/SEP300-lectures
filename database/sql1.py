from data import users
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db", echo=False)

with engine.begin() as conn:
    conn.exec_driver_sql("DROP TABLE IF EXISTS users")
    conn.exec_driver_sql("""
        CREATE TABLE users (
            user_id     INTEGER PRIMARY KEY,
            first_name  TEXT NOT NULL,
            last_name   TEXT NOT NULL,
            balance     NUMERIC(10,2) NOT NULL
        )
    """)

    for u in users:
        conn.exec_driver_sql(
            f"INSERT INTO users (user_id, first_name, \
                last_name, balance) "
            f"VALUES ({int(u['user_id'])}, \
                '{u['first_name']}', '{u['last_name']}', \
                    {float(u['balance']):.2f})"
        )
