import streamlit as st

st.title("Simple Chatbot")

# Ask user for their name
name = st.text_input("Enter your name:")

# Greet the user
if name:
    st.write(f"Hello {name}! 👋")
