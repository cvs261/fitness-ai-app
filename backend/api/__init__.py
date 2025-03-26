from flask import jsonify
from .recommend_api import recommend

def init_routes(app):
    app.add_url_rule("/api/recommend", view_func=recommend, methods=["POST"])
