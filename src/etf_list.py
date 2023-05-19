import requests
import pandas as pd
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

ENDPOINT = 'https://finance.naver.com/api/sise/etfItemList.nhn'

def get_etf_list(dto: EtfRequestDTO):
    res = requests.get(ENDPOINT, dto.params)
    # df.set_index('itemcode', inplace=True)
    # df = df[['itemcode', 'itemname']]
    return res.json()['result']['etfItemList']