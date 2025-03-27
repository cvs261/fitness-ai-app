import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_ENV"] = "testing"

from app import app
from extensions import db

class RecommendationAPITestCase(unittest.TestCase):
    def setUp(self):
        os.environ["FLASK_ENV"] = "testing"
        self.client = app.test_client()
        with app.app_context():
            db.create_all()  # ← creează toate tabelele în SQLite

    def tearDown(self):
        with app.app_context():
            db.drop_all()  # ← șterge tabelele după test, pentru curățenie

    def test_valid_recommendation(self):
        payload = {
            "Age": 25,
            "Gender": "Male",
            "Weight (kg)": 70,
            "Height (m)": 1.75,
            "BMI": 22.9,
            "Fat_Percentage": 15.0,
            "Experience_Level": 2,
            "Workout_Frequency (days/week)": 4,
            "Session_Duration (hours)": 1.0,
            "Calories_Burned": 500,
            "Max_BPM": 180,
            "Avg_BPM": 140,
            "Resting_BPM": 65,
            "Water_Intake (liters)": 2.0
        }

        response = self.client.post("/api/recommend", json=payload)
        print("->", response.json)
        self.assertEqual(response.status_code, 200)
        self.assertIn("recommended_workout", response.get_json())

    def test_missing_fields(self):
        payload = {
            "Age": 30,
            "Gender": "Female"
        }
        response = self.client.post("/api/recommend", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

if __name__ == "__main__":
    unittest.main()
