from .recommend_api import recommend

def init_routes(app):
    recommend(app)
