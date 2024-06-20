import streamlit as st
from pages.main_page import main_page
from pages.manage_conversations import manage_conversations_page
from utils.session_utils import initialize_session_state

# Initialize session state variables
initialize_session_state()

# Page navigation
page = st.sidebar.selectbox("Select Page", ["Main", "Manage Conversations"])

if page == "Main":
    main_page()
else:
    manage_conversations_page()

# Optional debug mode to display all message keys
debug_mode = st.checkbox("Debug Mode")
if debug_mode:
    st.write("Message Keys:")
    for idx, msg in enumerate(st.session_state.messages):
        st.write(f"{msg['content'][:10]}_{idx}: {msg['content']}")