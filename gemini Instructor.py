# app.py
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file at the start
load_dotenv()

# --- Gemini AI Configuration ---
# Configure the Google Generative AI library with the API key
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("Google AI API key not found. Please set the GOOGLE_AI_API_KEY in your .env file.")
        st.stop()
    genai.configure(api_key=api_key)
    
    # Initialize the Gemini model
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')

except Exception as e:
    st.error(f"Failed to configure or initialize Gemini AI: {e}")
    st.stop()


# --- Streamlit App UI ---
st.title("🌐 Gemini Translator")
st.caption("Translate any text into English using Gemini 1.5 Flash")
st.divider()

# The pre-prompt to instruct the model
pre_prompt = "Translate the following text into English: "

# User input using a text_area for longer text
prompt = st.text_area("Enter the text you want to translate:", height=150)
translate_button = st.button("Translate", use_container_width=True)

st.divider()

# --- Logic to handle the button click ---
if translate_button and prompt:
    # Combine the pre-prompt with the user's text
    full_prompt = pre_prompt + prompt
    
    with st.spinner("Translating..."):
        try:
            # Generate content using the Gemini model
            response = gemini_model.generate_content(full_prompt)
            
            # Display the translated text
            st.subheader("Translation:")
            st.markdown(response.text)
            st.balloons() # A little celebration!

        except Exception as e:
            # Handle potential errors during the API call
            st.error(f"An error occurred during translation: {e}")

elif translate_button and not prompt:
    st.warning("Please enter some text to translate.")

