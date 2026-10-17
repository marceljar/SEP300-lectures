from flask import (
    Flask, request, jsonify, render_template,
    redirect, url_for, session
)
from functools import wraps
import os

app = Flask(__name__)

# Required by Flask to sign session cookies.
app.secret_key = os.environ.get(
    "FLASK_SECRET_KEY",
    "classroom-demo-secret-change-me"
)

# Faculty credentials
faculty = {
    "marcel": "qwerty"
}

# In-memory database
students = [
    {"id": 101, "name": "Alice", "gpa": 3.8},
    {"id": 102, "name": "Bob", "gpa": 3.6}
]


def login_required(func):
    @wraps(func) # presevents Flask from losing the function name
    def wrapper(*args, **kwargs):
        if "faculty" not in session:
            return redirect(url_for("login"))

        return func(*args, **kwargs)

    return wrapper


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # Check username and password
        if faculty.get(username) == password:
            session.clear()
            session["faculty"] = username

            return redirect(url_for("students_page"))

        return render_template(
            "login.html",
            error="Invalid username or password"
        ), 401

    if "faculty" in session:
        return redirect(url_for("students_page"))

    return render_template("login.html")


@app.post("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.get("/students/<int:id>")
@login_required
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.post("/students")
@login_required
def add_student():
    new_student = request.get_json(silent=True)

    student_id = int(new_student["id"])
    name = str(new_student["name"]).strip()
    gpa = float(new_student["gpa"])

    student = {
        "id": student_id,
        "name": name,
        "gpa": gpa
    }

    students.append(student)
    return jsonify(student), 201


@app.put("/students/<int:id>")
@login_required
def update_student(id):
    updated_data = request.get_json(silent=True)

    for student in students:
        if student["id"] == id:
            changes = {}
            name = str(updated_data["name"]).strip()
            changes["name"] = name
            gpa = float(updated_data["gpa"])
            changes["gpa"] = gpa

            student.update(changes)
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.delete("/students/<int:id>")
@login_required
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted"})

    return jsonify({"error": "Student not found"}), 404


@app.get("/")
@login_required
def index():
    return redirect(url_for("students_page"))


@app.get("/students/view")
@login_required
def students_page():
    return render_template(
        "students.html",
        students=students
    )


@app.route("/students/add", methods=["GET", "POST"])
@login_required
def add_student_page():
    if request.method == "POST":
        new_student = {
            "id": request.form.get("id", type=int),
            "name": request.form.get("name", "").strip(),
            "gpa": request.form.get("gpa", type=float)
        }

        students.append(new_student)
        return redirect(url_for("students_page"))

    return render_template("add_student.html")


@app.get("/students/<int:id>/edit")
@login_required
def edit_student_page(id):
    for student in students:
        if student["id"] == id:
            return render_template(
                "edit_student.html",
                student=student
            )

    return "Student not found", 404
