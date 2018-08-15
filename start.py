#coding=utf-8
print("Start!")
# import homemade module and class
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
import Drawww
import Classs
# import module and class
import urllib.request as urllib2
import datetime
import numpy
import matplotlib.pyplot as plt
import pylab
import time
import random
# interactive part
StCo01 = str(input("Pls input the Stock Code(default 002597) ") or "002597")
Dura01 = int(input("How long? (default 200 days) ") or 200)
LT02   = int(input("Average duration (default 20 days) ") or 20)
InRa   = float(input("Rate (default 2) ") or 2)
ShTa   = str(input("Do you want to see the data table(Y/N)? (default Y)" )or "Y")
ShPc   = str(input("Do you want to see the Picture(Y/N)? (default Y)" )or "Y")
# get a stock object and get object's name
StSt = Classs.Stock(StCo01)
StNa01 = StSt.StockName
# get start and end date
Day01 = datetime.date.today()
Day02 = Day01 + datetime.timedelta(-int(Dura01))
Aa = Mathhh.NumberTo2DigitsToStr(Day02.month)
Bb = Mathhh.NumberTo2DigitsToStr(Day02.day)
Cc = Mathhh.NumberTo2DigitsToStr(Day02.year)
Day02YYYYMMDD = Cc + '-' + Aa + '-' + Bb
Dd = Mathhh.NumberTo2DigitsToStr(Day01.month)
Ee = Mathhh.NumberTo2DigitsToStr(Day01.day)
Ff = Mathhh.NumberTo2DigitsToStr(Day01.year)
Day01YYYYMMDD = Ff + '-' + Dd + '-' + Ee
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Get data from tushare to be a 2D data
Maxtrix01 = StSt.GetHistoryPrice(startt = Day02YYYYMMDD, endd = Day01YYYYMMDD)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#print basic info
print ("========================================================================")
print ("Stock: %s" % StCo01                                                      )
print ("Stock Name: %s" % StNa01                                                 )
print ("Duration: %s days" % Dura01                                              )
print ("Start: %s" % Day02YYYYMMDD                                               )
print ("End: %s" % Day01YYYYMMDD                                                 )
print ("Data from: %s" % "tushare"                                               )
print ("Average duration: %s" % LT02                                             )
print ("Judge Rate: %s" % InRa                                                   )
print ("Show detail data: %s" % ShTa.upper()                                     )
print ("Show Picture: %s" % ShPc.upper()                                         )
print ("========================================================================")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
# Get average of adj-value
Mathhh.Aver01(Maxtrix01, 2, LT02, "Average " + str(LT02) + " days",1)
#Get Difference
Mathhh.Diff01(Maxtrix01, 2, 7, "dif" ,1)
#Get average of Difference
Mathhh.Aver01(Maxtrix01, 8, LT02, "Ave. dif",1)
#Get biaozhuncha of Difference
Mathhh.Stdd01(Maxtrix01, 8, LT02, "STD",1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
# rate = dif / std
Mathhh.Rate01(Maxtrix01, 8, 10, "Rate",1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
# Set buy sell point
BP01 = BSP.GetBuyPoint01(Maxtrix01, 2, 7, 11, "Buy point", InRa, 1)
Tableee.Tableee01(BP01,2,0,MaxW = 6)
# Set sell point
BSP.GetSellPoint01(Maxtrix01, BP01[-1], 2, 7, "Sell point")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
# Show the table or not
if ShTa.lower() == "y":
    Tableee.Tableee01(Maxtrix01,2,0,MaxW = 6)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Show the picture or not
if ShPc.lower() == "y":
    Drawww.Draw01(Maxtrix01, StCo01, LT02)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>