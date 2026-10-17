from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "students.db"


# Connect to the database
def get_connection():
    conn = sqlite3.connect(DATABASE)
    # allows us to access the values using column names
    conn.row_factory = sqlite3.Row
    return conn


# Retrieve all students
@app.get("/students")
def get_students():
    conn = get_connection()
    students = conn.execute(
        "SELECT * FROM students"
        ).fetchall()
    conn.close()

    return jsonify([dict(student) for student in students])


# Retrieve a specific student
@app.get("/students/<int:id>")
def get_student(id):
    conn = get_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()

    conn.close()

    if student:
        return jsonify(dict(student))

    return jsonify({"error": "Student not found"}), 404


# Add a new student
@app.post("/students")
def add_student():
    new_student = request.get_json()

    conn = get_connection()

    conn.execute(
        "INSERT INTO students (id, name, gpa) VALUES (?, ?, ?)",
        (new_student["id"], new_student["name"], new_student["gpa"])
    )

    conn.commit()
    conn.close()

    return jsonify(new_student), 201


# Update an existing student
@app.put("/students/<int:id>")
def update_student(id):
    updated_data = request.get_json()

    conn = get_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()

    if student:
        # Preserve the original values for omitted fields
        name = updated_data.get("name", student["name"])
        gpa = updated_data.get("gpa", student["gpa"])

        conn.execute(
            "UPDATE students SET name = ?, gpa = ? WHERE id = ?",
            (name, gpa, id)
        )

        conn.commit()
        conn.close()

        return jsonify({"id": id, "name": name, "gpa": gpa})

    conn.close()
    return jsonify({"error": "Student not found"}), 404


# Delete a student
@app.delete("/students/<int:id>")
def delete_student(id):
    conn = get_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()

    if student:
        conn.execute(
            "DELETE FROM students WHERE id = ?", (id,)
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "Student deleted"})

    conn.close()
    return jsonify({"error": "Student not found"}), 404

