from .recommend_api import recommend
from auth import auth_bp

def init_routes(app):
    recommend(app)
    app.register_blueprint(auth_bp, url_prefix="/api")
