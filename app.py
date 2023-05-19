from src.etf_list import *
from src.enums import *
import streamlit as st

def filtering(etfList, kwd, volume = 0.5, cap = 0.5):
    kwd_filter = [f"name.str.contains('{k}')" for k in kwd]
    query = "category != 1 and not (" + " or ".join(kwd_filter) + ")"\
        + f" and trade_volume > {etfList.trade_volume.quantile(volume)}"\
        + f" and market_cap > {etfList.market_cap.quantile(cap)}"
    return etfList.query(query)

etfList = get_etf_list(
    EtfListRequestDTO(
        EtfType.전체,
        TargetColumn.시가총액
    )
)
kwd = ["레버리지", "2X", "금리", "단기채권", "단기통안채"]
st.dataframe(filtering(etfList, kwd, volume, cap))