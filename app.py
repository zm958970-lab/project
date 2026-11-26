import streamlit as st

st.set_page_config(page_title="Curiosity Lab")
st.title("Curiosity Lab")
st.header("探索你感兴趣的世界")
st.write("Curiosity Lab 帮你从一个感兴趣的主题出发，发现值得继续了解的问题。")

topic = st.text_input("请输入你感兴趣的主题", placeholder="例如：混沌理论")

if st.button("开始探索"):
    topic = topic.strip()
    if not topic:
        st.warning("请先输入一个你感兴趣的主题。")
    else:
        st.write(f"已收到你的探索主题：{topic}")
