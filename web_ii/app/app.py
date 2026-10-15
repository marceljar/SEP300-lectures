
from flask import Flask, request, jsonify, \
        render_template, redirect, url_for

app = Flask(__name__)

students = [
    {"id": 101, "name": "Alice", "gpa": 3.8},
    {"id": 102, "name": "Bob", "gpa": 3.6}
]


@app.get("/students")
def get_students():
    return jsonify(students)


@app.get("/students/<int:id>")
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.post("/students")
def add_student():
    new_student = request.get_json()

    if not isinstance(new_student, dict):
        return jsonify({"error": "Expected a JSON object"}), 400

    try:
        student_id = int(new_student["id"])
        name = str(new_student["name"]).strip()
        gpa = float(new_student["gpa"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Invalid student data"}), 400

    student = {"id": student_id, "name": name, "gpa": gpa}
    students.append(student)
    return jsonify(student), 201


@app.put("/students/<int:id>")
def update_student(id):
    updated_data = request.get_json()

    for student in students:
        if student["id"] == id:
            try:
                changes = {}

                if "name" in updated_data:
                    name = str(updated_data["name"]).strip()
                    changes["name"] = name

                if "gpa" in updated_data:
                    gpa = float(updated_data["gpa"])
                    changes["gpa"] = gpa

            except (ValueError, TypeError):
                return jsonify({"error": "Invalid student data"}), 400

            student.update(changes)
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.delete("/students/<int:id>")
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted"})

    return jsonify({"error": "Student not found"}), 404


@app.get("/")
def index():
    return redirect(url_for("students_page"))


@app.get("/students/view")
def students_page():
    return render_template("students.html", students=students)


@app.route("/students/add", methods=["GET", "POST"])
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
def edit_student_page(id):
    for student in students:
        if student["id"] == id:
            return render_template("edit_student.html", student=student)

    return "Student not found", 404

