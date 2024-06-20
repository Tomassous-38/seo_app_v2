import streamlit as st
from langchain_anthropic import ChatAnthropic
import os

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = None
    if 'llm' not in st.session_state:
        # Load environment variables from .env file
        from dotenv import load_dotenv
        load_dotenv()

        # Retrieve the Anthropic API key from environment variables
        ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

        # Initialize the Anthropic client
        st.session_state.llm = ChatAnthropic(
            model="claude-3-sonnet-20240229",  # Set a default model name
            api_key=ANTHROPIC_API_KEY,
            temperature=0.7,
            max_tokens=1024,
            timeout=None,
            max_retries=2,
        )

def reset_conversation_id():
    st.session_state.conversation_id = None

def clear_chat():
    st.session_state.messages = []
    st.session_state.conversation_id = None