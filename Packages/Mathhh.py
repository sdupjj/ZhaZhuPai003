#coding=utf-8
import numpy
import copy

def isNum(value):
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True

def NumberTo2DigitsToStr(value):
    if value >= 10:
        return str(value)
    else:
        return "0" + str(value)

def LimitedDisplay(value,width):
    a = str(value)
    if len(a)>width:
        return a[:width]
    else:
        return a

def Aver01(D2A, Col, Duration, Title, LineReduce = 1):
    Llength = len(D2A) - LineReduce + 1 
    D2A[0].append(str(Title))
    for Ll in range(1, Llength):
        if Llength - Ll >= Duration:
            CXL01 = []
            for i in range(Duration):
                if D2A[Ll+i][Col] != "n/a":
                    CXL01.append(float(D2A[Ll+i][Col]))
                else:
                    CXL01.append(D2A[Ll+i][Col])
            if "n/a" in CXL01:
                D2A[Ll].append("n/a")
            else: 
                D2A[Ll].append(str(sum(CXL01)/Duration))
        else:
            D2A[Ll].append("n/a")
            
def Diff01(D2A, Col1, Col2, Title, LineReduce = 1):
# Col2-Col1
    Llength = len(D2A)-LineReduce + 1
    D2A[0].append(Title) 
    for Ll in range(1, Llength):
        if ( D2A[Ll][Col2] != "n/a" ) and ( D2A[Ll][Col1] != "n/a" ) :
             D2A[Ll].append(str(float(D2A[Ll][Col2])-float(D2A[Ll][Col1])))
        else:
             D2A[Ll].append("n/a")

def Diff02(D2A, Col1, Col2, Title, LineReduce = 1):
# Col1-Col2
    Llength = len(D2A)-LineReduce + 1
    D2A[0].append(Title) 
    for Ll in range(1, Llength):
        if ( D2A[Ll][Col2] != "n/a" ) and ( D2A[Ll][Col1] != "n/a" ) :
             D2A[Ll].append(str(float(D2A[Ll][Col1])-float(D2A[Ll][Col2])))
        else:
             D2A[Ll].append("n/a")

def Diff03(D2A, Col1, Col2, Title, LineReduce = 1):
# 2 * ( Col1-Col2 )
    Llength = len(D2A)-LineReduce + 1
    D2A[0].append(Title) 
    for Ll in range(1, Llength):
        if ( D2A[Ll][Col2] != "n/a" ) and ( D2A[Ll][Col1] != "n/a" ) :
             D2A[Ll].append(str((float(D2A[Ll][Col1])-float(D2A[Ll][Col2]) )*2))
        else:
             D2A[Ll].append("n/a")


             
def Rate01(D2A, Col1, Col2, Title, LineReduce = 1):
# Col1 / Col2
    Llength = len(D2A)-LineReduce + 1
    D2A[0].append(Title)
    for Ll in range(1, Llength):
        if ( D2A[Ll][Col2] != "n/a" ) and ( D2A[Ll][Col1] != "n/a" ) and ( D2A[Ll][Col2] != 0 ):            
             D2A[Ll].append(str(float(D2A[Ll][Col1]) / float(D2A[Ll][Col2])))
        else:
             D2A[Ll].append("n/a")
             
def Stdd01(D2A, Col, Duration, Title, LineReduce = 1):
    Llength = len(D2A) - LineReduce + 1
    D2A[0].append(str(Title))
    for Ll in range(1, Llength):
        if Llength - Ll >= Duration:
            CXL01 = []
            for i in range(Duration):
                if D2A[Ll+i][Col] != "n/a":
                    CXL01.append(float(D2A[Ll+i][Col]))
                else:
                    CXL01.append(D2A[Ll+i][Col])
            if "n/a" in CXL01:
                D2A[Ll].append("n/a")
            else: 
                D2A[Ll].append(str(numpy.std(CXL01)))
        else:
            D2A[Ll].append("n/a")


