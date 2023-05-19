from src.etf_list import get_etf_list, filter_etf_list, FILTER_KWD
from src.history import get_history
from src.enums import *
from src.widget import quantile_slider, ban_kwd_expander
import streamlit as st

col1, col2 = st.columns(2)
with col1: quantile_slider("거래금액", "trade_volume", 0.7)
with col2: quantile_slider("시가총액", "market_cap", 0.7)

etfs = get_etf_list()
ban_kwd_expander(FILTER_KWD)
filtered_etfs = filter_etf_list(etfs)
# st.dataframe(
#     filtered_etfs,
#     height=250,
#     use_container_width=True)

if st.button("이력 불러오기"):
    st.write(filtered_etfs.ticker)