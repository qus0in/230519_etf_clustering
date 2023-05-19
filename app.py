from src.etf_list import get_etf_list, filter_etf_list
from src.enums import *
from src.widget import quantile_slider
import streamlit as st

quantile_slider("거래금액", "trade_volume", 0.7)
quantile_slider("시가총액", "market_cap", 0.7)

kwd = [
    "레버리지", "2X", "배당", "TRF", "TDF",
    "방어", "가치", "리츠", "은행", "보험", "증권",
    "금리", "단기채권", "단기통안채", "단기자금",
    "삼성", "ESG", "현대", "TSMC", "테슬라",
    "BBIG", "머니마켓", "혼합", "TIGER TOP10", 
    ]
etfs = get_etf_list()
st.dataframe(filter_etf_list(etfs, kwd),
             use_container_width=True)