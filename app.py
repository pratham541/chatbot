import streamlit as st

st.title("Simple Chatbot!")

# Ask the user to enter their name
name = st.text_input("Enter your name:")

# Display a greeting message
if name:
    st.write(f"Hello {name}!")
