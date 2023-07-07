import streamlit as st

# タイトルを表示する
st.title("Echo Chat UI")

# ユーザープロンプトがあれば、「こんにちは」というレスポンスを表示する
if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st.write("こんにちは")
