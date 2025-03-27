import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models import User
from extensions import db

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_register_user(self):
        response = self.client.post("/api/register", json={
            "email": "test@example.com",
            "password": "secret123"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("User registered successfully", response.get_json()["message"])

    def test_login_user(self):
        # Mai întâi înregistrăm
        self.client.post("/api/register", json={
            "email": "test@example.com",
            "password": "secret123"
        })

        response = self.client.post("/api/login", json={
            "email": "test@example.com",
            "password": "secret123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Logged successfully", response.get_json()["message"])

    def test_register_existing_user(self):
        self.client.post("/api/register", json={
            "email": "test@example.com",
            "password": "secret123"
        })
        response = self.client.post("/api/register", json={
            "email": "test@example.com",
            "password": "secret123"
        })
        self.assertEqual(response.status_code, 409)
        self.assertIn("Email already registered", response.get_json()["error"])

    def test_logout(self):
        self.client.post("/api/register", json={
            "email": "test@example.com",
            "password": "secret123"
        })
        self.client.post("/api/login", json={
            "email": "test@example.com",
            "password": "secret123"
        })
        response = self.client.post("/api/logout")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Logged out", response.get_json()["message"])

if __name__ == "__main__":
    unittest.main()
