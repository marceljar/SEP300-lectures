import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

first_name = input("Enter the user's first name: ")

# this is prone to SQL injection
# try using "' OR 1=1 --" as input
cursor.execute(
    f"SELECT user_id, first_name, last_name, balance "
    f"FROM users "
    f"WHERE first_name = '{first_name}'"
)

row = cursor.fetchone()

if row is None:
    print(f"No user with name {first_name}")
else:
    print("\nInfo about user:")
    print(f"{row[0]} {row[1]} {row[2]} {row[3]}")

conn.close()