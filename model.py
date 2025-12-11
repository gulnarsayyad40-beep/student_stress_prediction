import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    "study_hours": [1,2,3,4,5,6,7,8,9,10],
    "sleep_hours": [9,8,7,6,6,5,5,4,4,3],
    "assignments": [1,1,2,2,3,3,4,4,5,5],
    "social_media": [1,1,2,2,3,3,4,4,5,6],
    "exam_near": [0,0,0,1,1,1,1,1,1,1],
    "stress_level": ["Low","Low","Medium","Medium","Medium","High","High","High","High","High"]
}

df = pd.DataFrame(data)

X = df.drop("stress_level", axis=1)
y = df["stress_level"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved!")