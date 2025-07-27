# pages/Data_Visualization.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="📊 Data Visualization", page_icon="📈")
st.title("📊 :blue[Exploratory Data Analysis]")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""**Gain insights into the dataset used to train the spam detection model.**

This section helps you understand the characteristics of the SMS messages used in building our spam detection system. Through interactive charts and statistical summaries, you can explore the balance between spam and non-spam (ham) messages, analyze patterns in message length, and uncover trends that influenced the model's learning. By visualizing the dataset, we get a clearer picture of how text-based spam differs from legitimate communication — a crucial step in building effective NLP models.""")

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("data/spam.csv", encoding='latin-1')[['v1', 'v2']]
    data.columns = ['label', 'message']
    data['label_num'] = data['label'].map({'ham': 0, 'spam': 1})
    data['message_length'] = data['message'].apply(len)
    return data

df = load_data()

st.markdown("""-----""")

# Dataset preview
st.subheader("🗂 :blue[Dataset Overview]")
st.write(df.head())


st.markdown("""-----""")

# Label distribution pie chart
st.subheader("📌 :blue[Spam vs Ham Distribution]")
label_counts = df['label'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'orange'])
ax1.axis('equal')
st.pyplot(fig1)

st.markdown("""------""")

# Message length histogram
st.subheader("✉️ :blue[Message Length Distribution]")
fig2, ax2 = plt.subplots()
sns.histplot(data=df, x='message_length', hue='label', multiple='stack', palette='Set1', bins=40, ax=ax2)
ax2.set_title("Distribution of Message Length by Label")
st.pyplot(fig2)

st.markdown("""-------""")

# Summary statistics
st.subheader("📌 :blue[Average Message Length]")
spam_avg = df[df['label'] == 'spam']['message_length'].mean()
ham_avg = df[df['label'] == 'ham']['message_length'].mean()

st.markdown(f"- **Average Spam Message Length**: `{spam_avg:.2f}` characters")
st.markdown(f"- **Average Ham Message Length**: `{ham_avg:.2f}` characters")

st.markdown("""------""")

st.subheader("📩 :blue[You can download the Processed Dataset as a CSV file (Optional)]")

# Optional: download processed CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ :green[**Download Processed Dataset as CSV**]",
    data=csv,
    file_name='processed_spam_data.csv',
    mime='text/csv'
)
