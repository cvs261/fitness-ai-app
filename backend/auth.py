from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 409
    
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first
    if user and check_password_hash(user.password, password):
        session["user_id"] = user.id
        return jsonify({"message": "Logged successfully"}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    return jsonify({"message": "Logged out"}), 200