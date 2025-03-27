# backend/app.py

from flask import Flask
from flask_cors import CORS
from api import init_routes
from extensions import db, migrate
import os
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})



# Configurare DB în funcție de mediu
env = os.getenv("FLASK_ENV", "production")

if env == "testing" or app.config.get("TESTING"):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
else:
    DB_USER = os.getenv("DB_USER", "fitness_user")
    DB_PASS = os.getenv("DB_PASS", "fitness_pass")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "fitness_db")

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "super_secret_key_123"

db.init_app(app)
migrate.init_app(app, db)
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
