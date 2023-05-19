import streamlit as st

_LOAD_BUTTON_OPTION = {
    "label": "🔄 불러오기",
    "use_container_width" : True,
    "key": "run",
}

_CLEAR_BUTTON_OPTION = {
    "label": "🚿 리셋",
    "use_container_width" : True,
    "on_click": st.cache_data.clear,
}

def build():
    with st.sidebar:
        st.button(**_LOAD_BUTTON_OPTION)
        st.button(**_CLEAR_BUTTON_OPTION)