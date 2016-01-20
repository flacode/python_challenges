#returns the number of times a certain character appears in a gene
def gene(specimen):
    d={}
    for i in specimen:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

y=gene("AbcGgjhDhhd")
for i in y:
    print i+ ":" +str(y[i])
