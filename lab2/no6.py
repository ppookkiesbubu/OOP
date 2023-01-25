def add2list(ls1,ls2):
    return [ls1[i]+ls2[i] for i in range(0,len(ls1))]
print(add2list([1,2,3,4,5],[5,4,3,2,1]))