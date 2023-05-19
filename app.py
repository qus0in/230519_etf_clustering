from src.etf_list import get_etf_list, filter_etf_list
from src.history import get_history
from src.widget import sidebar
import streamlit as st

sidebar()

if st.session_state.run:
    with st.spinner("🫠 ETF 리스트를 불러오는 중입니다"):
        etfs = get_etf_list()
        filtered_etfs = filter_etf_list(etfs)

    histories = {}
    error = {}
    tickers = filtered_etfs.ticker
    progress_text = "🫠 거래 데이터를 불러오는 중입니다"
    bar = st.progress(0, text=progress_text)
    for idx in range(len(tickers)):
        ticker = tickers[idx]
        try:
            histories[ticker] = get_history(ticker, st.session_state.history_days)
        except:
            error[ticker] = filtered_etfs[filtered_etfs.ticker == ticker].item_name
        bar.progress((idx + 1) / len(tickers) * 100, text=progress_text)
    st.write(error)
else:
    st.info("ready...")
