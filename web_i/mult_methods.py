from flask import Flask, request, jsonify

app = Flask(__name__)

# Our "database" is simply a Python list
students = [
    {"id": 101, "name": "Alice", "gpa": 3.8},
    {"id": 102, "name": "Bob", "gpa": 3.6}
]


#@app.route("/students", methods=["GET"])
@app.get("/students")
def get_students():
    return jsonify(students)


#@app.route("/students", methods=["POST"])
@app.post("/students")
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201


#@app.route("/students/<int:id>", methods=["PUT"])
@app.put("/students/<int:id>")
def update_student(id):
    updated_data = request.get_json()

    for student in students:
        if student["id"] == id:
            student.update(updated_data)
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


#@app.route("/students/<int:id>", methods=["DELETE"])
@app.delete("/students/<int:id>")
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted"})

    return jsonify({"error": "Student not found"}), 404