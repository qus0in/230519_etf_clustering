from src.etf_list import get_etf_list, filter_etf_list, FILTER_KWD
from src.history import get_history
from src.enums import *
from src.widget import header
import streamlit as st

header()

etfs = get_etf_list()
filtered_etfs = filter_etf_list(etfs)
# st.dataframe(
#     filtered_etfs,
#     height=250,
#     use_container_width=True)

if st.button("이력 불러오기"):
    st.write(filtered_etfs.ticker)