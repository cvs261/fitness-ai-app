from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class RecommendationLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    result = db.Column(db.String(50))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        """ Hash the password and store it. """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """ Check hashed password """
        return check_password_hash(self.password, password)