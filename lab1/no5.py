a = []
for i in reversed(range(999)):
    for j in reversed(range(999)):
        k = str(i*j)
        m = k[0:int(len(k)/2)]
        n = k[int(len(k)/2):int(len(k))]
        o = n[::-1]
        if(m==o):
            a.append(k)
            b = list(map(int,a))
print(max(b))