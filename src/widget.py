import streamlit as st

def quantile_slider(label, key, default=0.5):
    SLIDER_OPTION = {
        "min_value" : 0.,
        "max_value" : 0.9,
        "step"      : 0.1,
        "value"     : default,
        "format"    : "%.1f"
    }
    st.slider(
        label=label + " 백분위수",
        key=key + "_quantile",
        **SLIDER_OPTION)

def ban_kwd_expander(kwd):
    with st.expander(f"제외 키워드 ({len(kwd)})"):
        st.write("🚫 " + " 🚫 ".join(kwd))