#coding=utf-8
import datetime

def GetBuyPoint01(D2A, Col1, Col2, Col3, Title = "Buy point", Rate = 2, LineReduce = 1):
#Col3 rate...
#Col1 Adj close
#Col2 Average of Adj close
#return a buy list
    
    Nowww = datetime.datetime.today()  
    Lll = [[99,99]]
    Llength = len(D2A) - LineReduce + 1
    D2A[0].append(Title)
    for Ll in range(1, Llength):
        TimeInTXT = datetime.datetime.strptime(D2A[1][0], '%Y-%m-%d')
        Gap01 = (Nowww - TimeInTXT).days
        if Gap01 > 10:
            for xxx in range(1, Llength):
                D2A[xxx].append(".")
            break
        if D2A[Ll][Col3] != "n/a":
            if float(D2A[Ll][Col3]) >= Rate:
                if float(D2A[Ll][Col1]) < float(D2A[Ll][Col2]):
                    D2A[Ll].append("BBB")
                    Lll.append([Ll,D2A[Ll][Col3]])
                else:
                    D2A[Ll].append(".")
            else:
                D2A[Ll].append(".")
        else:
            D2A[Ll].append(".")
    return Lll 
    
def GetSellPoint01(D2A, Start, Col1, Col2, Title, LineReduce = 1):
#return nothing
    Llength = len(D2A) - LineReduce + 1
    D2A[0].append(Title)
    Start = Start[0]
    if (Start >= 2) and (Start <= Llength):
        for Ll in range((Start-1),0,-1):
                if float(D2A[Ll][Col1]) > float(D2A[Ll][Col2]):
                    D2A[Ll].append("SSS")
                else:
                    D2A[Ll].append(".")               
        for Ll in range(Start, Llength):
            D2A[Ll].append(".")
    else:
        for Ll in range(1, Llength):
            D2A[Ll].append(".")
