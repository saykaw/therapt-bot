import chatbot
import streamlit as st
from streamlit_chat import message as st_message

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("MoMo")

if "history" not in st.session_state:
    st.session_state.history = []

def generate_answer():

    user_message = st.session_state.input_text
    st.session_state.history.append({"message": user_message, "is_user": True})

    answer = chatbot.reply(user_message)
    st.session_state.history.append({"message": answer, "is_user": False})

     # Reset the value of the input_text key to an empty string
    st.session_state.input_text = ""

st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

for i, chat in enumerate(st.session_state.history):
    st_message(message=chat["message"], is_user=chat["is_user"], key=str(i))


