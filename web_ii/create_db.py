import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        gpa REAL NOT NULL
    )
""")

# Five students to insert
students = [
    (101, "Alice", 3.8),
    (102, "Bob", 3.6),
    (103, "Charlie", 3.9),
    (104, "Diana", 3.5),
    (105, "Ethan", 3.7)
]

# Insert the students into the database
cursor.executemany("""
    INSERT OR REPLACE INTO students (id, name, gpa)
    VALUES (?, ?, ?)
""", students)

# Save changes and close the connection
conn.commit()
conn.close()

print("Database created and populated successfully!")
