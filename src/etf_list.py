import requests
import pandas as pd
import streamlit as st

from src.enums import *

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

def get_etf_list(dto: EtfListRequestDTO):
    df = pd.DataFrame(_get_data(dto.params)).iloc[:, [0, 1, 2, -2, -1]]
    df.rename(columns={
        "itemcode": "ticker",
        "etfTabCode": "category",
        "itemname": "name",
        "amonut": "trade_volume",
        "marketSum": "market_cap"
    }, inplace=True)
    return df

@st.cache_data
def _get_data(params: dict):
    ENDPOINT = 'https://finance.naver.com/api/sise/etfItemList.nhn'
    res = requests.get(ENDPOINT, params)
    data = res.json()['result']['etfItemList']
    return data