import streamlit as st
import joblib
import pandas as pd

with open('models/SpamDetectionSystem.pkl','rb')as file:
    model = joblib.load(file)

st.set_page_config(page_title='🏠SpamDetectionSystem_Home')

st.title(":blue[🚨 Spam Detection System Web App]")

st.write("Welcome to the :blue[**Spam Detection System**], a Machine Learning Web Application built using :blue[**Streamlit**] and powered by the :blue[**Naive Bayes Algorithm**]. This app is designed to classify text messages as either :red[**spam**] or :green[**not spam**] in real time, providing instant and reliable feedback. The primary goal of this project is to demonstrate how :blue[**Natural Language Processing (NLP)**] and classical machine learning techniques can be used to solve practical problems like spam detection. The system takes raw user input, cleans and transforms it into numerical format using :blue[**CountVectorizer**], and then feeds it into a pre-trained :blue[**Multinomial Naive Bayes Model**]. Based on the learned patterns from historical spam data, the model predicts whether the given message is likely to be spam. This app is ideal for learners exploring text classification, ML model deployment, and :blue[**interactive Python applications**]. With a minimal and responsive interface, users can interact with the model in real time, making it a useful tool for understanding how machine learning models function behind the scenes. Whether you're curious about how spam filters work, or you're learning how to deploy ML projects with Streamlit, this web app offers a hands-on, interactive experience.")


st.markdown("""



---
### :red[🔧 What Does It Do?]

This project demonstrates how Natural Language Processing (NLP) and Machine Learning (ML) can work together to filter out unwanted or potentially harmful messages. It simulates the core mechanism behind email or SMS spam filters using a clean and easy-to-use web interface.

When you enter a message into the input field, the following steps take place behind the scenes:

- 🔠 :blue[**Preprocessing and Vectorization**:] The input text is cleaned and transformed into numerical form using CountVectorizer, which converts words into a matrix of token counts. This step is essential because machine learning models cannot process raw text directly—they require numerical features.

- 🧠 :blue[**Model Prediction**:] The vectorized text is passed to a Multinomial Naive Bayes classifier, a probabilistic algorithm well-suited for text classification tasks. The model uses learned probabilities from training data to determine whether the message is more likely to be spam or not.

- ✅ :blue[**Result Display**:] Once the prediction is made, the app instantly displays the outcome—Spam or Not Spam—in a clear and visually distinct format. The minimal user interface ensures that even non-technical users can easily interact with the model and understand the result.

This entire process happens within a fraction of a second, allowing users to explore and understand how spam detection works in real-world systems. Whether you're testing a suspicious message or experimenting as part of your learning journey, this project offers a hands-on look at the power of ML in text classification.

---
### :green[🎯 Features]

- ✅ :blue[**Built with Python, Streamlit, and scikit-learn**]

Developed entirely using Python, this web app leverages the simplicity of Streamlit for UI and the power of scikit-learn for building and deploying machine learning models. It’s easy to understand, extend, and customize.

- ✅ :blue[**Naive Bayes Text Classification**]

Implements the Multinomial Naive Bayes algorithm, a proven method for spam detection and text classification tasks. This probabilistic model is known for its efficiency and accuracy, especially with word frequency–based inputs.

- ✅ :blue[**Instant, Real-Time Predictions**]

The app delivers predictions the moment you click the Predict button, making it highly responsive and practical. The backend processes the input, transforms it, runs the model, and displays the result—all in real time.

- ✅ :blue[**Clean, User-Friendly Interface**]

Designed with simplicity in mind, the interface allows users to interact with the model without needing any technical expertise. The layout is responsive, minimal, and easy to navigate on both desktop and mobile screens.

- ✅ :blue[**Educational and Demonstrative Tool**]

Ideal for students, beginners, or anyone learning NLP, ML, or model deployment. It offers hands-on exposure to how spam filters work and how machine learning models are built and served to end-users.

- ✅ :blue[**Lightweight and Easy to Deploy**]

No heavy setup required—this app runs smoothly with minimal dependencies and can be deployed locally or on platforms like Streamlit Cloud, Heroku, or Render.

- ✅ :blue[**Interpretable Results for Better Understanding**]

The app presents results in a clear and meaningful way, helping users understand not just what the model predicts, but how text-based models can process language data.

---
### :red[🚀 How to Use]

Using the **Spam Detection System Web App** is quick and straightforward. Follow the steps below to try it out:

1. :blue[**Navigate to the "Spam Checker" tab**]

Use the sidebar on the left-hand side of the screen to switch from the Home page to the Spam Checker section.

2. :blue[**Enter a message in the input field**]

Type or paste any text you want to analyze. It could be a line from an email, SMS, or any suspicious-looking message.

3. :blue[**Click the “Predict” button**]

Once your text is entered, click the Predict button to trigger the classification process.

4. :blue[**View the result instantly**]

The app will display whether your message is Spam or Not Spam in a bold, clear format—along with a color-coded response for better visual feedback.

This process takes only a few seconds and works entirely in real time. No technical knowledge is needed—just copy, paste, and predict!

---
### :green[👩‍💻 About This Project]

This web app was created as part of my personal learning journey in :blue[**Machine Learning and Natural Language Processing (NLP)**]. It serves not only as a hands-on project to deepen my understanding of text classification but also as a functional tool that others can use and learn from. By deploying the application publicly, my goal is to share this learning with a broader audience—especially students, developers, and tech enthusiasts who are exploring how classical ML models can be applied in real-world scenarios.

The core of the app is the :blue[**Naive Bayes classifier**], a lightweight yet powerful algorithm that has been widely used in spam filters due to its simplicity and effectiveness. Through this project, I implemented the end-to-end ML pipeline—from data preprocessing and feature extraction using :blue[**CountVectorizer**], to model training, evaluation, and deployment via :blue[**Streamlit**].

Making this project available online allows users to interact with a working ML model in real time, helping demystify the model-building and deployment process. It also reflects my growing proficiency in turning machine learning models into usable web applications and demonstrates the practical application of data science skills in building something that’s both educational and functional.

This app is open for public use, and feedback is always welcome to improve and expand its capabilities. It’s a small step toward building more intelligent systems and learning to bridge the gap between theory and real-world application.
""")






