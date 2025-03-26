from flask import Flask
from flask_cors import CORS
from api import init_routes

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
