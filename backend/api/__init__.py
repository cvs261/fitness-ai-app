from flask import jsonify

def init_routes(app):
    @app.route("/api/hello")
    def hello():
        return jsonify({"message": "Hello from Flask backend!"})
