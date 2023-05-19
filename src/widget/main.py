import streamlit as st
from PIL import Image
import os

from src.data.etf_list import *
from src.data.history import *
from src.widget.chart import *

def build():
    if st.session_state.run:
        
        with st.spinner("🫠 ETF 리스트를 불러오는 중입니다"):
            etfs = get_etf_list()
            filtered_etfs = filter_etf_list(etfs)

        history = load_history(filtered_etfs)
        with st.expander("덴드로그램"):
            corr_matrix = dendrogram(etfs.set_index('ticker'), history)
        with st.expander("실루엣 스코어"):
            best_number = silhouette(corr_matrix)
        st.write(best_number)
 
    else:
        image = Image.open('img/welcome.png')
        st.image(image)

_PROGERSS_TEXT = "🫠 거래 데이터를 불러오는 중입니다"

def bar():
    return st.progress(0, text=_PROGERSS_TEXT)

def load_history(filtered_etfs):
    error = []
    progress_bar = bar()
    tickers = filtered_etfs.ticker
    history = {}

    for idx in range(len(tickers)):
        ticker = tickers[idx]
        try:
            history[ticker] = get_history(ticker, st.session_state.history_days)
        except:
            error.append((ticker, filtered_etfs[filtered_etfs.ticker == ticker].iloc[0].item_name))
        rate = (idx + 1) / len(tickers)
        progress_bar.progress(rate, text=_PROGERSS_TEXT + f"({rate * 100:.2f}%)")
    
    progress_bar.empty()

    with st.expander(f"상장일 {st.session_state.history_days}일 미만"):
        st.dataframe(
            pd.DataFrame(error, columns=["종목코드", "종목명"]
                            ).set_index("종목코드"),
            height=250,
            use_container_width=True)
    st.write(history)
    return history
