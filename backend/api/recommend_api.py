from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from models import RecommendationLog

app = Flask(__name__)
CORS(app)

# Load model and encoders
model = joblib.load("ai/workout_model.joblib")
gender_encoder = joblib.load("ai/gender_encoder.joblib")
# goal_encoder = joblib.load("ai/goal_encoder.joblib")
# body_type_encoder = joblib.load("ai/body_type_encoder.joblib")
experience_encoder = joblib.load("ai/experience_encoder.joblib")
workout_encoder = joblib.load("ai/workout_encoder.joblib")

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.json

    try:
        # Encode categorical variables
        gender_encoded = gender_encoder.transform([data["Gender"]])[0]
        #goal_encoded = goal_encoder.transform([data["Goal"]])[0]
        #body_type_encoded = body_type_encoder.transform([data["Body_Type"]])[0]
        experience_encoded = experience_encoder.transform([data["Experience_Level"]])[0]

        # Create feature vector
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

        features = np.array(features).reshape(1, -1)

        # Predict and decode the result
        prediction = model.predict(features)[0]
        workout_type = workout_encoder.inverse_transform([prediction])[0]

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
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
