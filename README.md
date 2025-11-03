# 💰 Medical Insurance Cost Predictor

An interactive **Streamlit web app** that predicts individual **medical insurance charges** based on **age**, **BMI**, and **smoking habits** using the [Kaggle Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance).

---

## 🚀 Live Demo
*(https://medical-insurance-cost-predictor-fbgvddmpxnfilhuyamahmp.streamlit.app/)*  
👉 [Try it Online](#)

---

## 📊 Overview

This project uses a **machine learning regression model** trained on the *Medical Cost Personal Dataset* to estimate healthcare insurance costs.

Users can input:
- 🧍 **Age**
- ⚖️ **BMI (Body Mass Index)**
- 🚬 **Smoking Status**

and instantly get an estimated insurance cost, visualized through interactive charts.

---

## 🧠 Tech Stack

| Tool | Purpose |
|------|----------|
| **Python** | Core programming |
| **Streamlit** | Web app framework |
| **Pandas** | Data processing |
| **NumPy** | Numerical operations |
| **Matplotlib** | Data visualization |
| **Scikit-learn** | Machine learning model |
| **Joblib** | Model persistence |

---

## 🧩 How to Run Locally

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<parshva106>/<Medical-Insurance-Cost-Predictor>.git
cd <Medical-Insurance-Cost-Predictor>
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Streamlit app
bash
Copy code
streamlit run app.py
🧮 Model Details
The model is trained using:

Input Features (X): age, bmi, smoker_yes

Target Variable (y): charges

Example training setup:

python
Copy code
X = df_cleaned[['age', 'bmi', 'smoker_yes']]
y = df_cleaned['charges']
In the app, you can load your trained model:

python
Copy code
import joblib
model = joblib.load("insurance_model.pkl")
(A dummy model is included for demonstration so the app runs even without a saved model.)

📸 App Preview
Input Form	Output Example

📈 Example Prediction
Age	BMI	Smoker	Predicted Cost (₹)
25	22.4	No	₹11,500
45	30.2	Yes	₹32,800

✨ Features
✅ Simple and elegant UI
✅ Real-time prediction
✅ Visualization of input features
✅ Easily replaceable model file
✅ Fully deployable on Streamlit Cloud or Hugging Face

☁️ Deployment Guide
🔹 Streamlit Cloud
Go to streamlit.io/cloud

Connect your GitHub repo

Set the startup command:

arduino
Copy code
streamlit run app.py
🔹 Hugging Face Spaces
Create a new Space

Choose the Streamlit template

Upload your files (app.py, requirements.txt, and model)

Done 🎉

🧑‍💻 Author
Parshva Mehta
🎓 B.Tech in Electronics and Telecommunication
💼 Data Science & Machine Learning Enthusiast

🏷️ License
This project is licensed under the MIT License — feel free to use, modify, and share.

⭐ If you like this project, don’t forget to star the repo on GitHub!
