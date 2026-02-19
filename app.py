import streamlit as st
from agent import handle_query

# Page configuration
st.set_page_config(
    page_title="Drone Operations Coordinator AI",
    page_icon="🚁",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #FFFFFF;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 18px;
    color: #BBBBBB;
    text-align: center;
    margin-bottom: 30px;
}

.result-box {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #333;
    margin-top: 15px;
}

.footer {
    text-align: center;
    color: #888;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">🚁 Drone Operations Coordinator AI</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">AI assistant for managing pilots, drones, and mission coordination</div>',
    unsafe_allow_html=True
)

# Example queries
with st.expander("💡 Example queries you can try"):
    st.write("""
    • show available pilots  
    • show available drones  
    • detect conflicts  
    • find pilot with camera skill  
    """)

# Input box
query = st.text_input("Enter your query:", placeholder="Example: show available pilots")

# Button
if st.button("Submit Query", use_container_width=True):

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("Processing..."):
            response = handle_query(query)

        st.markdown("### 📋 Results")

        st.markdown(
            f'<div class="result-box">{response}</div>',
            unsafe_allow_html=True
        )

# Footer
st.markdown(
    '<div class="footer">Built using Streamlit • Google Sheets • AI Agent</div>',
    unsafe_allow_html=True
)
