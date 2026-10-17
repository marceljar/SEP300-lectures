from flask import ( Flask, request, jsonify, 
        render_template, redirect, url_for
)

app = Flask(__name__)

students = [
    {"id": 101, "name": "Alice", "gpa": 3.8},
    {"id": 102, "name": "Bob", "gpa": 3.6}
]

@app.get("/")
def index():
    return redirect(url_for("students_page"))


@app.get("/students/view")
def students_page():
    return render_template("students.html", students=students)


@app.post("/students")
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


@app.get("/students/<int:id>/edit")
def edit_student_page(id):
    for student in students:
        if student["id"] == id:
            return render_template(
                "edit_student.html", student=student
            )

    return "Student not found", 404


@app.put("/students/<int:id>")
def update_student(id):
    updated_data = request.get_json()

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
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted"})

    return jsonify({"error": "Student not found"}), 404


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

