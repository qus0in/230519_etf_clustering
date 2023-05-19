import FinanceDataReader as fdr
import streamlit as st

def get_history(code, days):
    df = _get_data(code)
    if len(df) < days:
        raise Exception("상장일 {days}일 미만")
    return df

@st.cache_data
def _get_data(code):
    return fdr.DataReader(code, start='2022')