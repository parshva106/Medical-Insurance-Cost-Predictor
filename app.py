import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle
import matplotlib.pyplot as plt

# Load the trained model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)
# ------------------------------------
# 🎨 App Configuration
# ------------------------------------
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------------------------
# 🧭 Header Section
# ------------------------------------
st.title("💰 Medical Insurance Cost Predictor")
st.markdown("""
### Predict your expected medical insurance charges
Enter your details below to get an estimated cost based on your **age**, **BMI**, and **smoking habits**.
""")

# Add a subtle divider
st.divider()

# ------------------------------------
# 🧠 Model Loading
# ------------------------------------
# If your model is saved, uncomment below:
# model = joblib.load("insurance_model.pkl")

# For demo (use a trained model if available)
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Dummy fit (so app runs without actual model file)
X_dummy = pd.DataFrame({
    'age': np.random.randint(18, 65, 100),
    'bmi': np.random.uniform(15, 35, 100),
    'smoker_yes': np.random.randint(0, 2, 100)
})
y_dummy = 1000 + 250*X_dummy['age'] + 300*X_dummy['bmi'] + 15000*X_dummy['smoker_yes']
model.fit(X_dummy, y_dummy)

# ------------------------------------
# 🎛️ Sidebar Inputs
# ------------------------------------
st.sidebar.header("🧍 User Inputs")

age = st.sidebar.slider("Age", 18, 65, 30)
bmi = st.sidebar.slider("BMI (Body Mass Index)", 15.0, 40.0, 25.0)
smoker = st.sidebar.radio("Are you a smoker?", ("No", "Yes"))

# Convert smoker to numeric
smoker_yes = 1 if smoker == "Yes" else 0

# ------------------------------------
# 📊 Prediction Section
# ------------------------------------
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'smoker_yes': [smoker_yes]
})

if st.button("💡 Predict Insurance Cost"):
    predicted_charge = model.predict(input_data)[0]
    
    st.success(f"### 💵 Estimated Insurance Cost: **₹{predicted_charge:,.2f}**")

    # Visualization: Feature Impact
    fig, ax = plt.subplots()
    features = ['Age', 'BMI', 'Smoker (Yes=1, No=0)']
    values = [age, bmi, smoker_yes]
    ax.bar(features, values)
    ax.set_title("📈 Your Input Values")
    ax.set_ylabel("Feature Value")
    st.pyplot(fig)

# ------------------------------------
# 💬 Footer
# ------------------------------------
st.markdown("---")
st.markdown("""
Made with ❤️ using Streamlit  
*Model trained on [Kaggle Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)*
""")
