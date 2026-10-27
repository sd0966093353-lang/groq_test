import streamlit as st
from groq import Groq

st.title("🤖 Groq 語意分析對話機器人")

# 初始化 Groq 客戶端 (從 Streamlit Secrets 讀取 API Key)
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("請先在 Streamlit Cloud 的 Settings -> Secrets 內設定 `GROQ_API_KEY`！")
    st.stop()

# 初始化對話歷史記錄 (存放在 st.session_state 裡，重新整理才不會消失)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一個樂於助人的 AI 助理，可以流暢地回答使用者提出的各種問題。"}
    ]

# 畫面渲染：顯示過去的所有對話記錄 (略過 system 提示詞)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 接收使用者的即時輸入
if user_input := st.chat_input("請輸入你想分析的句子（例如：Turn on the lights...）"):
    
    # 1. 將使用者的輸入加入歷史紀錄並顯示在畫面上
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. 呼叫 Groq 雲端模型進行對話
    with st.chat_message("assistant"):
        with st.spinner("AI 思考中..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.messages  # 帶入完整的對話上下文
                )
                assistant_reply = response.choices[0].message.content
                st.markdown(assistant_reply)
                
                # 3. 將 AI 的回答也加入歷史紀錄
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                
            except Exception as e:
                st.error(f"發生錯誤：{e}")