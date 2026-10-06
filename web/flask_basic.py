from flask import Flask, request, jsonify, abort
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
    return jsonify([row_to_dict(row) for row in rows]), 200


@app.get("/users/<int:user_id>")
def get_user(user_id):
    with engine.begin() as conn:
        query = "SELECT user_id, first_name, last_name, \
                 balance FROM users WHERE user_id = :id"
        result = conn.execute(text(query),
                     {"id": user_id},).mappings().first()
        if not result:
            abort(404, description="User not found.")
        return jsonify(row_to_dict(result)), 200


@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    with engine.begin() as conn:
        # Ensure user exists
        query = """
        SELECT user_id, first_name, last_name, balance 
        FROM users WHERE user_id = :id """
        result = conn.execute(text(query),\
                              {"id": user_id}).first()
        if not result:
            abort(404, description="User not found.")
        query = "DELETE FROM users WHERE user_id = :id" 
        conn.execute(text(query),{"id": user_id})
    return jsonify({"deleted": user_id}), 200


# Body:{"first_name": "", "last_name": "", "balance": 1.00}
@app.post("/users")
def create_user():
    data = request.get_json(silent=True) #data in JSON format
    #data = request.form.to_dict() #if data is from a form
    if data is None:
        abort(400, description="No application/json body.")
    for field in ("first_name", "last_name", "balance"):
        if field not in data:
            abort(400, description=f"Missing field: {field}")

    first_name = str(data["first_name"]).strip()
    last_name  = str(data["last_name"]).strip()
    balance    = float(data["balance"])

    if not first_name or not last_name:
        abort(400, description="names must be non-empty.")

    with engine.begin() as conn:
        query = """
         INSERT INTO users (first_name, last_name, balance)
         VALUES (:fn, :ln, :bal)"""
        result = conn.execute(text(query), \
         {"fn": first_name, "ln": last_name, "bal": balance})
        return "<p>User Inserted!</p>", 201
    

# Body: any subset of { "first_name", "last_name", "balance"}
@app.put("/users/<int:user_id>")
def update_user(user_id):
    data = request.get_json(silent=True) #data in JSON format
    #data = request.form.to_dict() #if data is from a form
    if data is None:
        abort(400, description="No application/json body.")
    
    with engine.begin() as conn:
        # Ensure user exists
        query = """
        SELECT user_id, first_name, last_name, balance 
        FROM users WHERE user_id = :id """
        result = conn.execute(text(query),\
                              {"id": user_id}).first()
        if not result:
            abort(404, description="User not found.")

        first_name = str(data["first_name"]).strip()
        last_name  = str(data["last_name"]).strip()
        balance    = float(data["balance"])
        
        query = """
          UPDATE users SET 
          first_name = :first_name, 
          last_name  = :last_name,
          balance    = :balance
          WHERE user_id = :id """
        conn.execute(text(query), {"first_name": first_name,\
                                   "last_name": last_name,\
                                   "balance": balance, \
                                   "id": user_id})
        return "<p>User updated</p>", 201


if __name__ == "__main__":
    app.run(debug=True)
