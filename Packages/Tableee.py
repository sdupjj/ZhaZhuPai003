#coding=utf-8
# This py module is to share some defs which can build Table based on a 2D data. 
#like [[1,2],[3,4]]
#       ||
#       ||
#   +-------+
#   +1  +2  +
#   +3  +4  +
#   +-------+
import Mathhh

def Tableee01(D2A,AddW = 2,LineReduce = 1,MaxW = 10):
    # default AddWidth = 2
    # default LineReduce 1 line
    try:
        # get every column width
        Llength = len(D2A)-LineReduce
        Wwidth = len(D2A[0])
        YYY = [0] * Wwidth
        for Ww in range(Wwidth):
            for Ll in range(Llength):    
                if len(str(D2A[Ll][Ww])) > YYY[Ww]:
                    YYY[Ww] = len(str(D2A[Ll][Ww]))
                    if YYY[Ww] > (MaxW-AddW):
                        YYY[Ww] = (MaxW-AddW)

        #print table line by line
        for Ll in range(Llength):
            print ("+" + "-" * sum(YYY)+ "-" * ( Wwidth * (AddW + 1) -1) + "+")
            Sets01 = 'print( '
            for Ww in range(Wwidth):
                Sets02 ="'|' + Mathhh.LimitedDisplay(D2A[Ll][" + str(Ww) + "],MaxW) + ' ' * (YYY[" + str(Ww) + "] + " + str(AddW) + " - len(str(D2A[Ll][" + str(Ww) + "]))) + "
                Sets01 = Sets01 + Sets02
            Sets01 = Sets01 + "'|')"
            exec(Sets01)
        print ("+" + "-" * sum(YYY)+ "-" * ( Wwidth * (AddW +1) -1) + "+")
    except TypeError:
        print ("+------------------------+")
        print ("|  Nothing can be shown  |")
        print ("+------------------------+")
    except IndexError:
        print ("+-----------------------------+")
        print ("|   99% INPUT DATA IS WRONG.  |")
        print ("+-----------------------------+")

def test01():
    x = [[1,2,3],[2,3,4],[4,1,5]]
    Tableee01(x,2,0)
    print ("...............")
    Tableee02(x,2,0,1,1,"N")
    print ("...............")
    Tableee01(x,2,0)
    y= [['date', 'open', 'close', 'high', 'low', 'volume', 'code']]
    Tableee01(y,2,0)
    print ("...............")

if __name__ == '__main__':
    test01()
