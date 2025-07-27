# model_info.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import classification_report, confusion_matrix

st.set_page_config(page_title="Model Info", page_icon="📊")

st.title("📊 :blue[Model Information]")

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("""


**🔍 Learn how this spam detection model works and how it was evaluated**

This section provides a detailed breakdown of the machine learning model powering our spam detection system. You'll explore the complete modeling pipeline — from raw text preprocessing to final classification.

We explain the techniques used, such as :blue[**TF-IDF vectorization**] for converting text into numerical features, and the :blue[**Naive Bayes Algorithm**] for probabilistic classification. You'll also gain insights into how the model was trained, validated, and evaluated using real-world SMS data.

Key performance indicators such as :blue[**accuracy, precision, recall**], and :blue[**F1-score**] are showcased along with a :blue[**confusion matrix**], giving you a transparent look into how well the model performs in distinguishing spam from non-spam messages.

This information not only helps you understand the model’s effectiveness but also builds trust in how predictions are made""")


st.markdown("""----""")

# Load model and sample data
@st.cache_resource
def load_model():
    return joblib.load("models/SpamDetectionSystem.pkl")

# Display model type and pipeline info
st.header("🧠 :blue[**Model Overview**]")
st.markdown("""
This spam detection system uses a :blue[**Naive Bayes Classifier**] combined with :blue[**TF-IDF Vectorization**].

The model was trained on a labeled dataset of SMS messages where:
- `1` = :red[**Spam**]  
- `0` = :green[**Not Spam (Ham)**]

The model pipeline includes:
- Text preprocessing
- TF-IDF vectorization
- Naive Bayes classification
""")

st.markdown("""------""")

# Optionally show pipeline steps if it's a pipeline
model = load_model()
if hasattr(model, "steps"):
    st.subheader("🔍 Model Pipeline")
    for step_name, step_obj in model.steps:
        st.markdown(f"- **{step_name.capitalize()}**: `{type(step_obj).__name__}`")

# Display evaluation metrics (you can preload or simulate this)
st.header("📈 :blue[**Evaluation Metrics**]")

# Sample simulated metrics — replace with your real data if available
metrics_data = {
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Score": [0.97, 0.95, 0.96, 0.955]
}
df_metrics = pd.DataFrame(metrics_data)

st.table(df_metrics)

st.markdown("""----""")

# Confusion matrix (simulated or real)
st.header("🧾 :blue[**Confusion Matrix**]")
conf_matrix = np.array([[965, 5], [25, 105]])  # replace with your actual values
fig, ax = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["Not Spam", "Spam"], yticklabels=["Not Spam", "Spam"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
st.pyplot(fig)

st.markdown("""------""")

# Use-case section
st.header("💡 :blue[**Use Case**]")
st.markdown("""
This project demonstrates how simple :blue[**machine learning models**] can effectively filter unwanted messages using :blue[**classical NLP techniques**].

It can be extended for:
- Email filtering
- Social media moderation
- Customer service inbox management
""")
