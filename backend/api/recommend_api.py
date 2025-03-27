from flask import request, jsonify
import joblib
import numpy as np
import pandas as pd
from models import RecommendationLog
from extensions import db

# Lazy load model and encoders
model = None
gender_encoder = None
workout_encoder = None

def load_assets():
    global model, gender_encoder, workout_encoder
    if model is None or gender_encoder is None or workout_encoder is None:
        try:
            model = joblib.load("backend/ai/workout_model.joblib")
            gender_encoder = joblib.load("backend/ai/gender_encoder.joblib")
            workout_encoder = joblib.load("backend/ai/workout_encoder.joblib")
        except FileNotFoundError as e:
            raise RuntimeError(f"Model or encoder file not found: {e}")

def recommend(app):
    @app.route("/api/recommend", methods=["POST"])
    def recommend_workout():
        try:
            load_assets()  # ensure model and encoders are loaded

            data = request.json

            # Encode categorical variable
            gender_encoded = gender_encoder.transform([data["Gender"]])[0]
            experience_encoded = data["Experience_Level"]

            features = [
                data["Age"],
                gender_encoded,
                data["Weight (kg)"],
                data["Height (m)"],
                data["Max_BPM"],
                data["Avg_BPM"],
                data["Resting_BPM"],
                data["Session_Duration (hours)"],
                data["Calories_Burned"],
                data["Fat_Percentage"],
                data["Water_Intake (liters)"],
                data["Workout_Frequency (days/week)"],
                experience_encoded,
                data["BMI"]
            ]

            input_df = pd.DataFrame([features], columns=[
                "Age", "Gender", "Weight (kg)", "Height (m)", "Max_BPM", "Avg_BPM", "Resting_BPM",
                "Session_Duration (hours)", "Calories_Burned", "Fat_Percentage", "Water_Intake (liters)",
                "Workout_Frequency (days/week)", "Experience_Level", "BMI"
            ])

            prediction = model.predict(input_df)[0]
            workout_type = workout_encoder.inverse_transform([prediction])[0]

            # Save to DB
            log = RecommendationLog(
                age=data["Age"],
                gender=data["Gender"],
                result=workout_type
            )
            db.session.add(log)
            db.session.commit()

            return jsonify({"recommended_workout": workout_type})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/api/history", methods=["GET"])
    def get_history():
        try:
            logs = RecommendationLog.query.all()
            history = [{
                "id": log.id,
                "age": log.age,
                "gender": log.gender,
                "result": log.result
            } for log in logs]
            return jsonify(history)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
