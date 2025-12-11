from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from pymongo import MongoClient

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["stressdb"]
records = db["predictions"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Collect input data from form
    study = float(request.form.get("study_hours"))
    sleep = float(request.form.get("sleep_hours"))
    assignment = float(request.form.get("assignments"))
    social = float(request.form.get("social_media"))
    exam_near = int(request.form.get("exam_near"))

    # Prepare array for model
    data = [study, sleep, assignment, social, exam_near]

    # Predict
    prediction = model.predict([data])[0]

    # Save to MongoDB
    records.insert_one({
        "study_hours": study,
        "sleep_hours": sleep,
        "assignments": assignment,
        "social_media": social,
        "exam_near": exam_near,
        "predicted_stress": prediction
    })

    # Go to NEXT PAGE with user-filled data + result
    return render_template(
        "result.html",
        study=study,
        sleep=sleep,
        assignments=assignment,
        social=social,
        exam=exam_near,
        result=prediction
    )

# ------------ Postman API ------------
@app.route("/api/predict", methods=["POST"])
def api_predict():
    body = request.get_json()

    data = [
        body["study_hours"],
        body["sleep_hours"],
        body["assignments"],
        body["social_media"],
        body["exam_near"]
    ]

    pred = model.predict([data])[0]

    records.insert_one({
        "input": data,
        "prediction": pred
    })

    return jsonify({"stress_level": pred})


if __name__ == "__main__":
    app.run(debug=True)