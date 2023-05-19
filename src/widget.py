import streamlit as st
from src.etf_list import FILTER_KWD

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

def header():
    col1, col2 = st.columns(2)
    with col1: quantile_slider("거래금액", "trade_volume", 0.7)
    with col2: quantile_slider("시가총액", "market_cap", 0.7)
    ban_kwd_expander(FILTER_KWD)