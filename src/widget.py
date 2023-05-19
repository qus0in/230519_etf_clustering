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
        st.write(", ".join(kwd))

def sidebar():
    with st.sidebar:
        quantile_slider("거래금액", "trade_volume", 0.7)
        quantile_slider("시가총액", "market_cap", 0.7)
        st.slider("상장일", key="history_days",
                  min_value=100, max_value=500, step=50, value=200)
        ban_kwd_expander(FILTER_KWD)
        st.button(**_BUTTON_OPTION)

_BUTTON_OPTION = {
    "label": "🔄 불러오기",
    "use_container_width" : True,
    "key": "run",
}