from flask import Flask, request, jsonify, abort, \
    render_template, redirect, url_for
from sqlalchemy import create_engine, text
from flask_cors import CORS

def row_to_dict(row):
    return {
        "user_id": row.user_id,
        "first_name": row.first_name,
        "last_name": row.last_name,
        "balance": float(row.balance),
    }

engine = create_engine("sqlite:///example.db", echo=False)

app = Flask(__name__)
CORS(app)  # allows for JavaScript origin

@app.get("/users")
def list_users():
    with engine.begin() as conn:
        query = "SELECT user_id, first_name, last_name, \
                 balance FROM users ORDER BY user_id"
        rows = conn.execute(text(query)).all()
    users = [row_to_dict(row) for row in rows]
    return render_template("users.html", users=users)


@app.get("/users/<int:user_id>")
def get_user(user_id):
    with engine.begin() as conn:
        query = "SELECT user_id, first_name, last_name, \
                 balance FROM users WHERE user_id = :id"
        result = conn.execute(text(query),
                     {"id": user_id},).mappings().first()
        if not result:
            abort(404, description="User not found.")
    user = row_to_dict(result)
    return render_template("user_details.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
