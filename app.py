import streamlit as st

# Đọc file index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Cấu hình trang
st.set_page_config(
    page_title="LG Spa Training Center",
    page_icon="✨",
    layout="wide"
)

# Hiển thị nội dung HTML
st.components.v1.html(html_content, height=2500, scrolling=True)
