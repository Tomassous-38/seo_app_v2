import streamlit as st
from utils.db_utils import get_saved_conversations, delete_conversation
from utils.session_utils import reset_conversation_id, clear_chat

def manage_conversations_page():
    st.title("Manage Saved Conversations")

    saved_conversations = get_saved_conversations()
    for conv in saved_conversations:
        st.write(f"ID: {conv[0]} | Title: {conv[1]} | Timestamp: {conv[2]}")
        if st.button(f"Load Conversation {conv[0]}", key=f"load_{conv[0]}"):
            clear_chat()
            st.session_state.conversation_id = conv[0]
            st.experimental_rerun()
        if st.button(f"Delete Conversation {conv[0]}", key=f"delete_{conv[0]}"):
            delete_conversation(conv[0])
            reset_conversation_id()  # Reset the conversation_id
            st.write(f"Conversation {conv[0]} deleted!")
            st.experimental_rerun()  # Refresh the page to show updated conversations