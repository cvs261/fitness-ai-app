from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
import os

# Load dataset
df = pd.read_csv("../ai/gym_members_exercise_tracking.csv")

# Drop rows with missing values
df.dropna(inplace=True)

# Encode categorical features
gender_encoder = LabelEncoder()
df["Gender"] = gender_encoder.fit_transform(df["Gender"])

workout_encoder = LabelEncoder()
df["Workout_Type"] = workout_encoder.fit_transform(df["Workout_Type"])

# Define features (based on available columns in dataset)
features = [
    "Age", "Gender", "Weight (kg)", "Height (m)", "Max_BPM", "Avg_BPM", "Resting_BPM",
    "Session_Duration (hours)", "Calories_Burned", "Fat_Percentage", "Water_Intake (liters)",
    "Workout_Frequency (days/week)", "Experience_Level", "BMI"
]

# Features (X) and target (y)
X = df[features]
y = df["Workout_Type"]

# Split dataset (optional for evaluation, but not used here)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
os.makedirs("ai", exist_ok=True)
joblib.dump(model, "backend/ai/workout_model.joblib")
joblib.dump(gender_encoder, "backend/ai/gender_encoder.joblib")
joblib.dump(workout_encoder, "backend/ai/workout_encoder.joblib")

print("Model and encoders trained and saved to 'ai/' folder.")
