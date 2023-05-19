from src.etf_list import get_etf_list, filter_etf_list
from src.enums import *
from src.widget import quantile_slider
import streamlit as st

quantile_slider("거래금액", "trade_volume")
quantile_slider("시가총액", "market_cap")

kwd = ["레버리지", "2X", "금리", "단기채권", "단기통안채"]
etfs = get_etf_list()
st.dataframe(filter_etf_list(etfs, kwd),
             use_container_width=True)