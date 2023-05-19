import requests
import pandas as pd
import streamlit as st

from src.enums import *

class EtfRequestDTO:
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

def get_etf_list(dto: EtfRequestDTO):
    df = pd.DataFrame(_get_data())
    return df.iloc[:, [0, 1, 2, -2, -1]]

@st.cache
def _get_data(params):
    ENDPOINT = 'https://finance.naver.com/api/sise/etfItemList.nhn'
    res = requests.get(ENDPOINT, dto.params)
    data = res.json()['result']['etfItemList']
    return data