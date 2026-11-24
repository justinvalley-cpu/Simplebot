import streamlit as st

st.title("🤖 SimpleBot")

message = st.chat_input("Type a message")

if message:
    st.chat_message("user").write(message)

    if "hello" in message.lower():
        response = "Hey there! Ready to write some Python?"
    elif "joke" in message.lower():
        response = "Why do programmers prefer dark mode? Because light attracts bugs!"
    else:
        response = "I'm still learning!"

    st.chat_message("assistant").write(response)
