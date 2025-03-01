import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

st.title(":green[Simple] Definitions 🎉")
st.markdown("### Happy Birthday, Mommy!")
st.write(
    "I made this app for you because you don't know some definitions of words. "
    "This app will help you find simple definitions easily!"
)

# User input
user_prompt = st.text_input("Enter a word:", placeholder="Your Word goes Here")

# Generate response
if user_prompt:
    with st.spinner("Generating definition..."):
        try:
            response = model.generate_content(
                f"Give me a simple definition all in one sentence: {user_prompt}",
                stream=True
            )
            response_text = "".join(chunk.text for chunk in response if hasattr(chunk, "text") and chunk.text)
            
            if response_text.strip():
                st.success(response_text)
            else:
                st.warning("No definition found. Try another word!")

        except Exception as e:
            st.error(f"Error: {str(e)}")

st.caption("Made by Taksha")
