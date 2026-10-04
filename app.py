import streamlit as st
from google import genai
from google.genai import types

# -----------------------------
# Gemini setup
# -----------------------------
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

# -----------------------------
# App title
# -----------------------------
st.title("👗 AI Wardrobe & Outfit Stylist")

st.write(
    "Upload a photo of your outfit or clothes and get personalized "
    "styling suggestions from AI."
)

# -----------------------------
# Upload image
# -----------------------------
uploaded_image = st.file_uploader(
    "📸 Upload a photo of your clothes",
    type=["jpg", "jpeg", "png"]
)

# Show uploaded image
if uploaded_image:
    st.image(
        uploaded_image,
        caption="Your uploaded photo",
        use_container_width=True
    )

# -----------------------------
# User question
# -----------------------------
user_message = st.chat_input(
    "What should I wear today?"
)

# -----------------------------
# Send image + question to Gemini
# -----------------------------
if user_message:

    if uploaded_image:

        image_bytes = uploaded_image.getvalue()

        prompt = f"""
You are a helpful personal fashion stylist.

Analyze the clothing shown in the uploaded image.

The user asked:
{user_message}

Give practical outfit advice based on the clothes visible in the image.

Tell the user:
1. What they can wear
2. What combinations would look good
3. What they should avoid
4. Why you recommend the outfit

Keep the answer simple, friendly, and useful for everyday college life.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=uploaded_image.type
                ),
                prompt
            ]
        )

        st.subheader("🤖 Your AI Stylist")
        st.write(response.text)

    else:

        st.warning(
            "📸 Please upload a photo first so I can analyze your clothes."
        )