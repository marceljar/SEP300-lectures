from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# run with Flask's built-in development server with: 
# flask --app minimal.py run