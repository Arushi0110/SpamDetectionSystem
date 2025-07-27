import streamlit as st
import joblib
import re
import string
import os

# Page configuration
st.set_page_config(page_title="Detect Spam")

# Page Title
st.title(":blue[🛡️ Spam Message Detector]")


st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
Use this tool to detect whether a given message is :red[**Spam**] or :green[**Not Spam**] using a trained :blue[Naive Bayes Classifier].
""")

# --- Load Combined Model + Vectorizer ---
@st.cache_resource
def load_model():
    with open('models/SpamDetectionSystem.pkl','rb')as file:
      data = joblib.load(file)

    if isinstance(data, dict):  # If saved as a dictionary
        model = data['model']
        vectorizer = data['vectorizer']
    elif isinstance(data, tuple):  # If saved as tuple
        model, vectorizer = data
    else:
        raise ValueError("Unknown format of SpamDetectionSystem.pkl")
    
    return model, vectorizer

model, vectorizer = load_model()

# --- Preprocessing Function ---
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

# --- User Input ---
user_input = st.text_area("✉️ **Enter the message you want to check:**")

# --- Predict Button ---
if st.button("🔍 :blue[**Predict for Spam**]"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to analyze.")
    else:
        cleaned_text = preprocess_text(user_input)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)
        probability = model.predict_proba(vectorized_text)[0]

        # --- Show Result ---
        if prediction[0] == 1:
            st.markdown("""
                <div style="padding: 1rem; background-color: #ffe6e6; border-left: 5px solid red;">
                    <h3 style="color: red;">🚫 Spam Message Detected!</h3>
                    <p><strong>Confidence:</strong> {:.2f}%</p>
                </div>
            """.format(probability[1] * 100), unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="padding: 1rem; background-color: #e6ffec; border-left: 5px solid green;">
                    <h3 style="color: green;">✅ Legitimate Message (Not Spam)</h3>
                    <p><strong>Confidence:</strong> {:.2f}%</p>
                </div>
            """.format(probability[0] * 100), unsafe_allow_html=True)

# --- Example Button ---
st.markdown("---")
if st.button("🧪 :green[**Try Example Message**]"):
    example_msg = "Congratulations! You've won a free voucher. Click here to claim now."
    st.info(f"Example Message: {example_msg}")

    cleaned_example = preprocess_text(example_msg)
    vectorized_example = vectorizer.transform([cleaned_example])
    example_pred = model.predict(vectorized_example)
    example_proba = model.predict_proba(vectorized_example)[0]

    if example_pred[0] == 1:
        st.markdown("""
            <div style="padding: 1rem; background-color: #ffe6e6; border-left: 5px solid red;">
                <h3 style="color: red;">🚫 Spam Message Detected!</h3>
                <p><strong>Confidence:</strong> {:.2f}%</p>
            </div>
        """.format(example_proba[1] * 100), unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="padding: 1rem; background-color: #e6ffec; border-left: 5px solid green;">
                <h3 style="color: green;">✅ Legitimate Message (Not Spam)</h3>
                <p><strong>Confidence:</strong> {:.2f}%</p>
            </div>
        """.format(example_proba[0] * 100), unsafe_allow_html=True)
