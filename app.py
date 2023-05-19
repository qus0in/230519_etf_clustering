from src.etf_list import get_etf_list, filter_etf_list
from src.history import get_history
from src.widget import sidebar

import streamlit as st
import pandas as pd

sidebar()

if st.session_state.run:
    with st.spinner("🫠 ETF 리스트를 불러오는 중입니다"):
        etfs = get_etf_list()
        filtered_etfs = filter_etf_list(etfs)

    histories = {}
    error = []
    tickers = filtered_etfs.ticker
    progress_text = "🫠 거래 데이터를 불러오는 중입니다"
    bar = st.progress(0, text=progress_text)
    for idx in range(len(tickers)):
        ticker = tickers[idx]
        try:
            histories[ticker] = get_history(ticker, st.session_state.history_days)
        except:
            error.append((ticker, filtered_etfs[filtered_etfs.ticker == ticker].iloc[0].item_name))
        bar.progress((idx + 1) / len(tickers), text=progress_text)
    st.subheader(f"상장일 {st.session_state.history_days}일 미만")
    st.dataframe(pd.DataFrame(error, columns=["종목코드", "종목명"]))
    bar.empty()
else:
    st.info("ready...")
