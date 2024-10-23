import pyttsx3
import streamlit as st

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 1)    # Volume 0-1

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Streamlit app setup
st.title("Text-to-Speech Converter")
st.write("Enter the text below and click 'Convert to Speech' to hear it spoken aloud.")

# Create a text input area for the user
text_input = st.text_area("Enter Text", value="Hello, this is a text-to-speech test.", height=150)

# Button to trigger text-to-speech conversion
if st.button("Convert to Speech"):
    if text_input.strip():
        # Call the text_to_speech function
        text_to_speech(text_input)
        st.success("Text has been converted to speech.")
    else:
        st.error("Please enter some text to convert.")
