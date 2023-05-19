from enum import Enum

class EtfType(Enum):
    전체 = 0
    국내시장지수 = 1
    국내업종테마 = 2
    국내파생 = 3
    해외주식 = 4
    원자재 = 5
    채권 = 6
    기타 = 7

class TargetColumn(Enum):
    현재가 = 'now_val'
    전일비 = 'change_val'
    등락률 = 'change_rate'
    NAV = 'nav'
    삼개월수익률 = '3month_earn_rate'
    거래량 = 'acc_quant'
    거래대금 = 'acc_amount'
    시가총액 = 'market_sum'