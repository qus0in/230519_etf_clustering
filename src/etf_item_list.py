import requests
from src.enums import *

class EtfItemDTO:
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

def get_etf_item_list(dto: EtfItemDTO):
    res = requests.get(ENDPOINT, dto.params)
    return res.json()['result']['etfItemList']