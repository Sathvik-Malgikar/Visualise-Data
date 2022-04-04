from matplotlib import pyplot 
def baralg(vl):
    itemlist=list(range(1,len(vl)+1))
    vl=list(map(float,vl)) 
    pyplot.bar(itemlist,vl)
    return pyplot.show()

