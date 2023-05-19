from src.etf_list import *
from src.enums import *
import streamlit as st

etfList = get_etf_list(
    EtfListRequestDTO(
        EtfType.전체,
        TargetColumn.시가총액
    )
)
kwd = ["레버리지", "2X", "금리"]
query = [f"name.str.contains('{k}')" for k in kwd]
fillteredEtfList = etfList.query(
    "category != 1 and not (" + " or ".join(query) + ")"
)
st.dataframe(fillteredEtfList)