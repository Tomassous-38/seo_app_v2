import streamlit as st
from utils.db_utils import save_new_conversation, save_message, get_messages
from utils.response_utils import generate_response, reset_state, prompt_template
from utils.session_utils import reset_conversation_id, clear_chat

def main_page():
    st.title("SEO Article Brief Generator")

    # User inputs for keyword, sources, and client priority
    keyword = st.text_input("Target Keyword (in French)")
    sources = st.text_area("Relevant Sources")
    client_priority = st.text_area("Client Priority")

    # Model and temperature selection
    model = st.selectbox(
        "Select Model",
        [
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
            "claude-2.1",
            "claude-2.0",
            "claude-instant-1.2"
        ]
    )
    temperature = st.slider("Select Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.number_input("Max Tokens", min_value=1, max_value=4000, value=1024)

    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = None

    # Clear button action
    if st.button("Clear"):
        clear_chat()
        st.rerun()

    if st.session_state.conversation_id is not None:
        # Display existing messages if a conversation is loaded
        messages = get_messages(st.session_state.conversation_id)
        for message in messages:
            with st.chat_message(message[0]):
                st.markdown(message[1])

    # Generate brief button action
    if st.button("Générer le Brief"):
        reset_state()
        reset_conversation_id()  # Ensure conversation_id is reset
        title = f"Conversation {st.session_state.conversation_id if st.session_state.conversation_id else 'new'}"
        st.session_state.conversation_id = save_new_conversation(title)
        prompt = prompt_template.format(keyword=keyword, sources=sources, client_priority=client_priority)
        st.session_state.messages.append({"role": "user", "content": prompt})
        generate_response(prompt, model, temperature, max_tokens)
        save_message(st.session_state.conversation_id, "user", prompt)

    # Chat input for additional remarks to improve the brief
    if prompt := st.chat_input("Enter your remarks or ask a question to improve the brief:"):
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        generate_response(prompt, model, temperature, max_tokens)
        save_message(st.session_state.conversation_id, "user", prompt)

    # Display the messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            save_message(st.session_state.conversation_id, message["role"], message["content"])

    # Add a "Save Conversation" button
    if st.button("Save Conversation"):
        full_conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
        if st.session_state.conversation_id is None:
            st.session_state.conversation_id = save_new_conversation(full_conversation)
        st.write("Conversation saved!")