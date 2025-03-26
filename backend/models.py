from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RecommendationLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    result = db.Column(db.String(50))
