# backend/app.py
from flask import Flask
from flask_cors import CORS
from api import init_routes
from extensions import db 
import os

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Use SQLite for testing, MariaDB in production
if os.getenv("FLASK_ENV") == "testing":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fitness_user:fitness_pass@db/fitness_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
