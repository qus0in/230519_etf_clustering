from src.etf_list import *
from src.enums import *
import streamlit as st

etfList = get_etf_list(
    EtfListRequestDTO(
        EtfType.전체,
        TargetColumn.시가총액
    )
)
kwd = ["레버리지", "2X", "금리", "단기채권", "단기통안채"]
kwd_filter = [f"name.str.contains('{k}')" for k in kwd]
fillteredEtfList = etfList.query(
    "category != 1 and not (" + " or ".join(kwd_filter) + ")"
    + f" and trade_volume > {etfList.trade_volume.mean()}"
    + f" and market_cap > {etfList.market_cap.quantile(.5)}"
)
st.dataframe(fillteredEtfList)