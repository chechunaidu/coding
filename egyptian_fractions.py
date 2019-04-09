import math
def printEgyptianFractions(nr,dr):
    ef=[]
    
    while(nr!=0):
        x=math.ceil(dr/nr)
        ef.append(x)
        nr=nr*x-dr
        dr=dr*x
    for i in range(len(ef)):
        if(i!=len(ef)-1):
            print("1/{0}+".format(ef[i]),end=' ')
        else:
            print("1/{0}".format(ef[i]),end=" ")
printEgyptianFractions(8,15)