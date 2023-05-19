from src.etf_list import *
from src.enums import *
import streamlit as st

etfList = get_etf_list(
    EtfListRequestDTO(
        EtfType.전체,
        TargetColumn.시가총액
    )
)
kwd = ["레버리지"]
fillteredEtfList = etfList.query(
    "category != 1 and (@kwd in name)"
)
st.dataframe(fillteredEtfList)