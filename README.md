# 🎓 Student Stress Level Prediction  
A Machine Learning + Flask web application that predicts a student's stress level based on their daily study habits.  
The project includes:

- Flask backend  
- ML prediction model  
- MongoDB database  
- Attractive HTML UI with background image  
- API support (Postman testing)  

---

## 🚀 Features  
✔ Predicts student stress level  
✔ Clean and responsive UI  
✔ Data stored in MongoDB  
✔ Result shown on a new page  
✔ API endpoint for Postman testing  
✔ Well-structured Flask project  

---

## 🧠 Tech Stack  
**Frontend**  
- HTML 

**Backend**  
- Python  
- Flask  

**Database**  
- MongoDB

**Machine Learning**  
- Scikit-learn  
- Pickle model  

---

## 📂 Project Structure

student-stress-predictor/ │ ├── app.py ├── model.pkl ├── requirements.txt │ ├── templates/ │   ├── index.html │   └── result.html │ └── static/  └── bg.jpg

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/student-stress-predictor.git cd student-stress-predictor

### 2️⃣ Create Virtual Environment

python -m venv venv venv\Scripts\activate   (Windows)

### 3️⃣ Install Requirements

pip install -r requirements.txt

### 4️⃣ Run the App

python app.py

Open the browser:

http://127.0.0.1:5000

---

## 🗄 MongoDB Setup  
1. Install MongoDB
2. Replace your MongoDB URI in `app.py`:

```python
client = MongoClient("your_mongo_uri_here")

3. Data will be stored in:



stressdb → predictions


---

🧪 API (Postman) Testing

POST Request

URL:

http://127.0.0.1:5000/api/predict

JSON Body Example

{
  "sleep_hours": 7,
  "study_hours": 4,
  "exams_near": 1
}

Response

{
  "predicted_stress": "High"
}



---

🧑‍💻 Author

Gulnar Sayyad