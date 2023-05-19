import streamlit as st

def quantile_slider(label, key):
    SLIDER_OPTION = {
        "min_value" : 0.,
        "max_value" : 0.9,
        "step"      : 0.1,
        "value"     : 0.5,
        "format"    : "%.1f"
    }
    st.slider(
        label=label + " 백분위수",
        key=key + "_quantile",
        **SLIDER_OPTION)