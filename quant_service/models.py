#-*- coding: utf-8 -*-

from mongoengine import *
# connect('quant_base', host='localhost', port=27017)

class Stocks_Info(Document):
    sid = IntField(required=True)
    code = IntField(required=True)
    name = StringField(required=True)
    aggrv = StringField(required=True)  # 中文首字母
    spell = StringField(required=True)  # 中文全拼
    meta = {'collection': 'stocks_info'}

class Stock_Data(Document):
    sid = IntField(required=True)
    code = IntField(required=True)
    open = FloatField(required=True)
    close = FloatField(required=True)
    high = FloatField(required=True)
    low = FloatField(required=True)
    trade_date = DateTimeField(required=True)
    volume = IntField(required=True)
    price_change = FloatField(required=True)
    p_change = FloatField(required=True)
    ma5 = FloatField(required=True)
    ma10 = FloatField(required=True)
    ma20 = FloatField(required=True)
    v_ma5 = FloatField(required=True)
    v_ma10 = FloatField(required=True)
    v_ma20 = FloatField(required=True)
    turnover = FloatField(required=True)
    meta = {'collection': "stock_data"}

    def tojson(self):
        return {
            'open':self.open,
            'code':self.code
        }
