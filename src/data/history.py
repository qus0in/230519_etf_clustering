import FinanceDataReader as fdr
import streamlit as st
import pandas as pd

def get_history(code, days):
    df = _get_data(code)
    if len(df) < days:
        raise Exception(f"상장일 {days}일 미만")
    return df

@st.cache_data(show_spinner=False)
def _get_data(code):
    return fdr.DataReader(code, start='2022')

def get_earning_rate(df: pd.DataFrame):
    df_er = df.rolling(20).apply(lambda x: (x[-1] - x[0]) / x[0]).dropna()
    df_er.columns = [df.loc[idx].item_name for idx in df_er.columns]
    return df_er
