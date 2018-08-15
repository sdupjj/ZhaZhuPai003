#coding=utf-8
import os
import sys
import platform
if platform.system()== "Windows":
    SiGNN = "\\"
else:
    SiGNN = "/"
Dirr01 = os.getcwd()    
sys.path.append(Dirr01)
sys.path.append(Dirr01 + SiGNN + "Packages")

import Tableee
import Mathhh
import BSP
import tushare as tu

class Stock(object):
	def __init__(self,StockNumber):
		self.StockNumber = StockNumber
		self.StockName = tu.get_realtime_quotes(str(self.StockNumber))['name'][0]

	def CurrentPrice(self):
		a = tu.get_realtime_quotes(str(self.StockNumber))
		b = a['price']
		c = a['time']
		self.CurrentPrice = float(b[0])
		self.CurrentPriceTime = c[0]
		return self.CurrentPrice
		
	def GetHistoryPrice(self,startt,endd):
		original_HistoryPrice = tu.get_k_data(str(self.StockNumber), autype='qfq',start=startt,end=endd)
		data_HistoryPrice = original_HistoryPrice.values.tolist()
		title_HistoryPrice = original_HistoryPrice.columns.values.tolist()
		data_HistoryPrice.append(title_HistoryPrice)
		data_HistoryPrice.reverse()
		self.HistoryPrice = data_HistoryPrice
		return self.HistoryPrice
