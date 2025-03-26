from flask import Flask
from flask_cors import CORS
from api import init_routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

init_routes(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://fitness_user:fitness_pass@db/fitness_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
