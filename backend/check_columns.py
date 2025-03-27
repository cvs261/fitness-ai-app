import pandas as pd

df = pd.read_csv("../ai/gym_members_exercise_tracking.csv")

print("Available columns: ")
print(df.columns.tolist())