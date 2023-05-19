from src.etf_list import *
from src.enums import *
import streamlit as st

etfList = get_etf_list(
    EtfListRequestDTO(EtfType.전체,
                  TargetColumn.시가총액)
).query("category != 1")
st.dataframe(etfList)