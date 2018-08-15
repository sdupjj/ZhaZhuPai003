import datetime
import numpy
import matplotlib.pyplot as plt
import pylab
import Mathhh


def Draw01(D2A, StockName, Duration):
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
	# show as a picture
	# x axis, time
	Llength = len(D2A) - 1 
	CXL02 = []
	for Ll in range(1, Llength):
	    CXL02.append(datetime.datetime.strptime(D2A[Ll][0], '%Y-%m-%d'))
	CXL02.reverse()
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# y axis, adj close value 
	CXL03 = []
	for Ll in range(1, Llength):
	    CXL03.append(float(D2A[Ll][2]))
	CXL03.reverse()
	Label03 = D2A[0][2]
	# Buy piont
	CXL06 = []
	CXL07 = []
	for Ll in range(1, Llength):
	    if D2A[Ll][12] == "BBB":
	        CXL06.append(datetime.datetime.strptime(D2A[Ll][0], '%Y-%m-%d'))
	        CXL07.append(float(D2A[Ll][2]))
	CXL06.reverse()
	CXL07.reverse()
	#---------------------------------------
	# Sell point
	CXL08 = []
	CXL09 = []
	for Ll in range(1, Llength):
	    if D2A[Ll][13] == "SSS":
	        CXL08.append(datetime.datetime.strptime(D2A[Ll][0], '%Y-%m-%d'))
	        CXL09.append(float(D2A[Ll][2]))
	CXL08.reverse()
	CXL09.reverse()
	#---------------------------------------
	# volumn
	CXL10 = []
	for Ll in range(1, Llength):
	    CXL10.append(int(D2A[Ll][5]))
	CXL10.reverse()
	#---------------------------------------
	plt.figure(1)
	ax1 =  plt.subplot(211)
	ax2 =  plt.subplot(212)
	plt.sca(ax1)
	plt.plot(CXL02, CXL03, color = "black", label = Label03)
	plt.plot_date(pylab.date2num(CXL06), CXL07)
	plt.plot_date(pylab.date2num(CXL08), CXL09, color = "red")
	plt.title(StockName + " + Average " + str(Duration) + " + Buy / Sell point ")
	plt.sca(ax2)
	plt.plot(CXL02,CXL10)
	plt.title(" Vol. ")
	plt.show()

