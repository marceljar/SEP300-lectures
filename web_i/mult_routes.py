from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Website!</h1>"

@app.route("/about")
def about():
    return "<p>This is a simple Flask application.</p>"

@app.route("/contact")
def contact():
    return "<h1>Contact Us</h1><p>contact@example.com</p>"

# run with Flask's built-in development server with: 
# flask --app mult_routes.py run