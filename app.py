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

    if 'history' not in st.session_state:
        st.session_state['history'] = {}
    
    error = []
    tickers = filtered_etfs.ticker
    progress_text = "🫠 거래 데이터를 불러오는 중입니다"
    bar = st.progress(0, text=progress_text)
    for idx in range(len(tickers)):
        ticker = tickers[idx]
        try:
            st.session_state.history[ticker] = get_history(ticker, st.session_state.history_days)
        except:
            error.append((ticker, filtered_etfs[filtered_etfs.ticker == ticker].iloc[0].item_name))
        bar.progress((idx + 1) / len(tickers), text=progress_text)
    bar.empty()
    with st.expander(f"상장일 {st.session_state.history_days}일 미만"):
        st.dataframe(
            pd.DataFrame(error, columns=["종목코드", "종목명"]
                            ).set_index("종목코드"),
            height=250,
            use_container_width=True)
    
    st.info("set...")

else:
    st.info("ready...")
