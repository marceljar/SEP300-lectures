from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///example.db", echo=False)

with engine.connect() as conn:
    print("\nAll users:")
    result = conn.execute(
        text("SELECT user_id, first_name, last_name, balance "
             "FROM users ORDER BY user_id")
    )
    for row in result:
        print(row.user_id, row.first_name, \
              row.last_name, row.balance)

with engine.connect() as conn:
    row = conn.execute(
        text("""
            SELECT user_id, first_name, last_name, balance
            FROM users
            WHERE user_id = 1
        """)).one_or_none()

if row is None:
    print(f"No user with id 1")

print("\nInfo about first user:")
print(f"{row.user_id} {row.first_name} \
      {row.last_name} {row.balance}")

with engine.connect() as conn:
    print("\nUsers with balance >= 100.00 (first_name, \
          last_name, balance):")
    result = conn.execute(
        text("SELECT first_name, last_name, balance "
             "FROM users WHERE balance >= 100.00 \
                ORDER BY balance DESC")
    )
    for row in result:
        print(row.first_name, row.last_name, row.balance)

with engine.begin() as conn:
    conn.execute(
        text("UPDATE users SET balance = balance + 10.0 \
             WHERE user_id = 1")
    )
    conn.execute(
        text("UPDATE users SET last_name = 'Thompson' \
             WHERE user_id = 2")
    )

with engine.connect() as conn:
    print("\nAfter updates (Alice, Bob):")
    result = conn.execute(
        text("SELECT user_id, first_name, last_name, balance "
             "FROM users WHERE user_id IN (1,2) \
                ORDER BY user_id")
    )
    for row in result:
        print(row.user_id, row.first_name, \
              row.last_name, row.balance)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM users \
                      WHERE user_id = 12"))
    conn.execute(text("DELETE FROM users \
                      WHERE balance < 10.0"))

with engine.connect() as conn:
    print("\nRemaining users:")
    result = conn.execute(
        text("SELECT user_id, first_name, last_name, balance "
             "FROM users ORDER BY user_id")
    )
    for row in result:
        print(row.user_id, row.first_name, \
              row.last_name, row.balance)
