import mysql.connector

# note that different users might have different level of access
# passwords are frequently retrieved from other files
conn = mysql.connector.connect(
    host="localhost",
    user="marcel",
    password="your_password_here",
    database="example"
)

cursor = conn.cursor()

print("\nAll users:")
cursor.execute(
    "SELECT user_id, first_name, last_name, balance "
    "FROM users ORDER BY user_id"
)

for row in cursor.fetchall():
    print(row[0], row[1], row[2], row[3])


cursor.execute("""
    SELECT user_id, first_name, last_name, balance
    FROM users
    WHERE user_id = 1
""")

row = cursor.fetchone()

if row is None:
    print("No user with id 1")
else:
    print("\nInfo about first user:")
    print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


print("\nUsers with balance >= 100.00 "
      "(first_name, last_name, balance):")

cursor.execute(
    "SELECT first_name, last_name, balance "
    "FROM users WHERE balance >= 100.00 "
    "ORDER BY balance DESC"
)

for row in cursor.fetchall():
    print(row[0], row[1], row[2])


cursor.execute(
    "UPDATE users SET balance = balance + 10.0 "
    "WHERE user_id = 1"
)

cursor.execute(
    "UPDATE users SET last_name = 'Thompson' "
    "WHERE user_id = 2"
)

conn.commit()


print("\nAfter updates (Alice, Bob):")

cursor.execute(
    "SELECT user_id, first_name, last_name, balance "
    "FROM users WHERE user_id IN (1,2) "
    "ORDER BY user_id"
)

for row in cursor.fetchall():
    print(row[0], row[1], row[2], row[3])


cursor.execute(
    "DELETE FROM users "
    "WHERE user_id = 12"
)

cursor.execute(
    "DELETE FROM users "
    "WHERE balance < 10.0"
)

conn.commit()


print("\nRemaining users:")

cursor.execute(
    "SELECT user_id, first_name, last_name, balance "
    "FROM users ORDER BY user_id"
)

for row in cursor.fetchall():
    print(row[0], row[1], row[2], row[3])


cursor.close()
conn.close()