from flask import Flask
from models import db
from app import app

with app.app_context():
    db.create_all()
    print("Tabele create cu succes.")
