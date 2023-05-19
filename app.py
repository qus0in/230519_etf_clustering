from src.etf_list import *
from src.enums import *
import streamlit as st

def filtering(etfList, kwd, volume = 0.5, cap = 0.5):
    kwd_filter = [f"name.str.contains('{k}')" for k in kwd]
    query = "category != 1 and not (" + " or ".join(kwd_filter) + ")"\
        + f" and trade_volume > {etfList.trade_volume.quantile(st.session_state.trade_volume_quantile)}"\
        + f" and market_cap > {etfList.market_cap.quantile(st.session_state.market_cap_quantile)}"
    return etfList.query(query)

st.slider(
    min_value=0, max_value=1, step=0.1, value=0.5, key="trade_volume_quantile")
st.slider(
    min_value=0, max_value=1, step=0.1, value=0.5, key="market_cap_quantile")
kwd = ["레버리지", "2X", "금리", "단기채권", "단기통안채"]
etfList = get_etf_list(
    EtfListRequestDTO(
        EtfType.전체,
        TargetColumn.시가총액
    )
)

st.dataframe(filtering(etfList, kwd))