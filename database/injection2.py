from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///example.db", echo=False)

first_name = input("Enter the user's first name: ")

with engine.connect() as conn:
    row = conn.execute(
        text(f"SELECT user_id, first_name, last_name, balance\
            FROM users \
            WHERE first_name = :first_name"),\
            {"first_name": first_name}).first()

if row is None:
    print(f"No user with name {first_name}")
else:
    print("\nInfo about user:")
    print(f"{row.user_id} {row.first_name} \
          {row.last_name} {row.balance}")

