import requests
import pandas as pd
import streamlit as st

from src.data.enums import *
from src.data.constants import *

class EtfListRequestDTO:
    def __init__(self,
                 etfType: EtfType,
                 targetColumn: TargetColumn) -> None:
        self.etfType = etfType
        self.targetColumn = targetColumn
        self.sortOrder = "desc"
    
    @property
    def params(self):
        return {
            "etfType": self.etfType.value,
            "targetColumn": self.targetColumn.value,
            "sortOrder": self.sortOrder
        }

def get_etf_list(dto: EtfListRequestDTO=None):
    if dto is None:
        dto = EtfListRequestDTO(
            EtfType.전체,
            TargetColumn.시가총액
        )
    df = pd.DataFrame(_get_data(dto.params)).iloc[:, [0, 1, 2, -2, -1]]
    df.rename(columns={
        "itemcode": "ticker",
        "etfTabCode": "category",
        "itemname": "item_name",
        "amonut": "trade_volume",
        "marketSum": "market_cap"
    }, inplace=True)
    return df

def filter_etf_list(etfList):
    kwd_filter = [f"item_name.str.contains('{k}')" for k in FILTER_KWD]
    category = [2]
    query1 = "(category in @category) and not (" + " or ".join(kwd_filter) + ")"
    eftList2 = etfList.query(query1)
    query2 = f"trade_volume > {eftList2.trade_volume.quantile(st.session_state.trade_volume_quantile)}"\
        + f" and market_cap > {eftList2.market_cap.quantile(st.session_state.market_cap_quantile)}"
    return .query(query2).reset_index(drop=True)

@st.cache_data(show_spinner=False)
def _get_data(params: dict):
    ENDPOINT = 'https://finance.naver.com/api/sise/etfItemList.nhn'
    res = requests.get(ENDPOINT, params)
    data = res.json()['result']['etfItemList']
    return data