# First
import openai 
import streamlit as st

#openai_api_key = st.secrets['OPENAI_TOKEN']

with st.sidebar:
    user_name = st.text_input("Nome de usuário", key="user_name", type="default")
    openai_api_key = st.text_input("Token API", key="token_openai", type="password")
    "[Site OpenAI](https://platform.openai.com)"    
    "[Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)"

st.title("💬 ELIZA Reboot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": """You are ELIZA, chatbot created 1966. If you know this chatbot start the conversation presenting your self as ELIZA your online therapeut, don't need to describe what ELIZA is, and neither describe when created.
All the following interactions has to be answered with ELIZA answers when possible"""}]
    st.session_state.messages.append({"role": "assistant", "content": "Type your message to start your therapeut support"})
    

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)