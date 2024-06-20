import time
import streamlit as st

# Function to reset the session state (clear chat history and reset conversation ID)
def reset_state():
    st.session_state.messages = []
    st.session_state.conversation_id = None

# Function to build the conversation history
def build_conversation_history():
    conversation = [("system", "You are an SEO content specialist. Improve the brief based on the user's instructions without adding any extra comments.")]
    for msg in st.session_state.messages:
        conversation.append((msg["role"], msg["content"]))
    return conversation

# Generator function to yield chunks of response text
def response_generator(response_text):
    for word in response_text.split():
        yield word + " "
        time.sleep(0.05)  # Adjust delay for streaming effect

# Function to generate a response and update session state
def generate_response(prompt, model, temperature, max_tokens):
    conversation = build_conversation_history()
    conversation.append(("user", prompt))
    
    # Update the model parameters with user-selected values
    st.session_state.llm.model = model
    st.session_state.llm.temperature = temperature
    st.session_state.llm.max_tokens = max_tokens
    
    response = st.session_state.llm.invoke(conversation)
    assistant_response = response.content
    
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    # Stream the response in the chat
    with st.chat_message("assistant"):
        response_stream = st.write_stream(response_generator(assistant_response))

# Define the prompt template
prompt_template = """
You will act as an SEO content specialist to create a comprehensive, SEO-optimized brief for a writer who will be tasked with writing an article on the keyword I provide. The Keyword will be in French, and the brief will be in French.
Here is the target keyword to optimize the article brief for:
<keyword>
{keyword}
</keyword>

Structure the brief in markdown format, using <hn> tags to outline the sections and subsections the article should include. Under each <hn> heading, provide detailed bullet points covering the specific elements, information, and topics that section of the article should discuss.

To help with researching and gathering relevant information for the brief, I will provide some sources, which may include academic articles or other pertinent articles:
<sources>
{sources}
</sources>

Be very thorough and detailed in fleshing out the brief. I may provide additional remarks or suggestions to help improve and refine the brief.

In addition to the content outline, please suggest the following SEO meta elements:
- <title>
- Meta description
- <h1>
These meta elements should all include the target keyword, adhere to Google's recommended lengths, accurately reflect the article's content, and have an informative tone suitable for a long-form educational article.

Here is the client's key business priority that should be tied into the article where most relevant and natural:
<client_priority>
{client_priority}
</client_priority>

Provide your finished brief inside <brief> tags. Remember, the goal is to create an in-depth, well-structured outline that will guide the writer in creating a comprehensive, SEO-optimized article on the given keyword.
"""