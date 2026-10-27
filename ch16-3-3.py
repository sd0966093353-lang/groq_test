import streamlit as st
from groq import Groq

# 從 Streamlit Secrets 讀取 API Key (或直接填入你的 Groq API Key)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

prompt1 = "請分析句子 '"
prompt2 = "' 的語意含義，是「開」還是「關」。答案僅用一個字表達。"
text_to_analyze = "Turn on the lights in the room."
question = prompt1 + text_to_analyze + prompt2

st.write("Q:", question)

# 呼叫 Groq 雲端模型 (支援 llama-3.1-8b-instant)
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "你是語意分析機器人"},
        {"role": "user", "content": question}
    ]
)

result = response.choices[0].message.content
st.write("Result:", result)