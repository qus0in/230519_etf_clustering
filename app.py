from src.etf_list import get_etf_list, filter_etf_list
from src.history import get_history
from src.widget import sidebar
import streamlit as st

sidebar()

etfs = get_etf_list()
filtered_etfs = filter_etf_list(etfs)
# st.dataframe(
#     filtered_etfs,
#     height=250,
#     use_container_width=True)

if st.button("불러오기", use_container_width=True):
    st.write(filtered_etfs.ticker)