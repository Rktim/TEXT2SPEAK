import streamlit as st
import pyttsx3

def main():
    st.title("Text 2 Speak")
    
    user_input = st.text_input("Enter your desired text:")
    
    if st.button("Say some!!"):
        engine = pyttsx3.init()
        engine.say(user_input)
        engine.runAndWait()

if __name__ == '__main__':
    main()