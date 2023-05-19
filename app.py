from src.etf_list import get_etf_list, filter_etf_list
from src.history import get_history
from src.widget import sidebar
import streamlit as st

sidebar()

if st.session_state.run:
    etfs = get_etf_list()
    filtered_etfs = filter_etf_list(etfs)

    histories = {}
    error = {}
    for ticker in filtered_etfs.ticker:
        try:
            histories[ticker] = get_history(ticker, st.session_state.history_days)
        except:
            error[ticker] = filtered_etfs[filtered_etfs.ticker == ticker].name[0]

    st.write(error)
else:
    st.info("ready...")
