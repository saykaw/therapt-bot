import chatbot
import streamlit as st

# Add a CSS stylesheet to style the app
st.markdown("""
    <style>
        .chat-message {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 10px;
            max-width: 80%;
        }
        .chat-message-user {
            background-color: #e6f7ff;
            align-self: flex-start;
        }
        .chat-message-bot {
            background-color: #d9d9d9;
            align-self: flex-end;
        }
    </style>
""", unsafe_allow_html=True)

st.title("MoMo")

# Create a two-column layout for the chat input and output
input_col, history_col = st.beta_columns([3, 7])

# Add a text input to get the user message
with input_col:
    st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

    # Add a button to submit the user message
    input_col.button("Send")

# Create a container to hold the chat history
with history_col:
    history_container = st.beta_container()

    # Add a header to the chat history container
    history_container.header("Chat History")

    # Display the chat history using the streamlit_chat message component
    with history_container:
        for i, chat in enumerate(st.session_state.history):
            if chat["is_user"]:
                st.markdown(f'<div class="chat-message chat-message-user">{chat["message"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message chat-message-bot">{chat["message"]}</div>', unsafe_allow_html=True)

# Define a function to generate the chatbot's response
def generate_answer():
    user_message = st.session_state.input_text
    st.session_state.history.append({"message": user_message, "is_user": True})

    answer = chatbot.reply(user_message)
    st.session_state.history.append({"message": answer, "is_user": False})
