from src.etf_item_list import *
from src.enums import *
import streamlit as st

etfItemList = get_etf_item_list(
    EtfItemDTO(EtfType.전체, TargetColumn.시가총액)
)
df = pd.DataFrame(etfItemList)
df.set_index('itemcode', inplace=True)
df.drop(inplace=True, labels=["etfTabCode", "risefall"], axis=1)
st.dataframe(etfItemList)