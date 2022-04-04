from functools import reduce
from matplotlib import pyplot
def pialg(vl,list_l):
    itemlist=[]
    for i in range(len(vl)):
        itemlist.append(list_l[i].get())
    pyplot.pie(vl,labels=itemlist)
    return pyplot.show()

 