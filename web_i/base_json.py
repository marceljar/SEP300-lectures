from flask import Flask, jsonify

app = Flask(__name__)

# Data stored in a Python dictionary
students = [
    {
        "id": 101,
        "name": "Alice",
        "program": "Computer Programming",
        "gpa": 3.8
    },
    {
        "id": 102,
        "name": "Bob",
        "program": "Software Engineering",
        "gpa": 3.6
    }
]

@app.route("/")
def home():
    return "<h1>Welcome to My Website!</h1>"

@app.route("/student")
def get_student():
    return jsonify(students)

# run with Flask's built-in development server with: 
# flask --app base_json.py run