import streamlit as st
import requests

st.set_page_config(page_title="HAI-Sentinel Helpdesk", layout="wide")
st.title("🤖 HAI-Sentinel: GenAI Helpdesk Intelligence")

query = st.text_input("अपना सवाल यहाँ लिखें:")
if st.button("Generate Insight"):
    if query:
        response = requests.get(f"http://backend:8000/ask?query={query}").json()
        st.subheader("AI Insight:")
        st.success(response["answer"])
        with st.expander("Sources & Logs"):
            st.write(response["sources"])
