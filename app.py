import streamlit as st
from google import genai

# Get Gemini API key
api_key = st.secrets["GEMINI_API_KEY"]

# Create Gemini client
client = genai.Client(api_key=api_key)

st.title("👗 AI Wardrobe & Outfit Stylist")

st.write("Ask me anything about your outfit!")

# User input
user_message = st.chat_input("What should I wear today?")

if user_message:
    st.write("You asked:", user_message)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_message
    )

    st.write("🤖 Stylist:", response.text)