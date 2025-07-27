import streamlit as st
from datetime import datetime
import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

# --- Page Config ---
st.set_page_config(page_title="💬 Feedback", layout="centered")

# --- Google Sheets Setup ---
def append_to_google_sheet(name, rating, comments):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # ✅ Load creds from secrets (gcp_service_account section)
    creds_dict = st.secrets["gcp_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)

    client = gspread.authorize(creds)
    spreadsheet = client.open("Diabetes Feedback")  # this is the Spreadsheet object
    spreadsheet.share('pariarushi01@gmail.com', perm_type='user', role='writer')
    
    sheet = spreadsheet.sheet1

    row = [name, rating, comments, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    sheet.append_row(row)

# --- Title ---
st.title(":blue[💬 We Value Your Feedback!]")
st.markdown("<br>", unsafe_allow_html=True)

# --- Info Text ---
st.markdown("""
    Please share your thoughts about the :blue[**Spam Detection App**].
    Your feedback helps us improve! 😊
""")

# --- Feedback Form ---
with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("👤 **Your Name (optional)**")
    rating = st.number_input("⭐ **Rate the App (1 = Poor, 5 = Excellent)**", min_value=1, max_value=5, step=1)
    comments = st.text_area("📝 **Your Feedback**")

    submit = st.form_submit_button(":green[**Submit Message**]")

# --- Save to Google Sheet ---
if submit:
    if not name:
        name = "Anonymous"

    try:
        append_to_google_sheet(name, rating, comments)
        st.success("✅ Feedback submitted successfully!")

        with st.expander("📋 Your Submitted Feedback"):
            st.json({
                "Name": name,
                "Rating": rating,
                "Comments": comments,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    except Exception as e:
        st.error(f"❌ Failed to submit feedback: {e}")
