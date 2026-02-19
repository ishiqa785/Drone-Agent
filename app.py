import streamlit as st
from agent import handle_query

st.title("Drone Operations Coordinator AI")

user_input = st.text_input("Ask your question:")

if user_input:
    response = handle_query(user_input)
    st.text(response)
