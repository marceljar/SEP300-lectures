from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Website!</h1>"

@app.route("/about")
def about():
    return "<h1>About Us</h1><p>This is a simple Flask application.</p>"

@app.route("/contact")
def contact():
    return "<h1>Contact Us</h1><p>Email us at contact@example.com</p>"

# run with Flask's built-in development server with: 
# flask --app mult_routes.py run