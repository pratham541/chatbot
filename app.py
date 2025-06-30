import streamlit as st
import os

st.title("Simple Chatbot")

# Ask user for their name
name = st.text_input("Enter your name:")

# Greet the user
if name:
    st.write(f"Hello {name}! 👋")

# Configure Streamlit to run on port 8000 if deployed on Azure
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    import streamlit.web.bootstrap
    streamlit.web.bootstrap.run("app.py", "", [], port=port)
