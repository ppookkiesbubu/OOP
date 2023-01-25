a = input()
b = a.split()
c = list(map(int,b))
d = c[2]-c[0]
e = c[3]-c[1]
total = 0
if(e<=15 and d==0):
    total = 0
elif(d>=6 and e>0):
    total = 200
elif(d==0 and e>15):
    total = 10
elif(0<d<=6 and e==0):
    for i in range(d):
        if(i<4):
            total += i*10
        if(4<=i<=6):
            total += i*20
elif(0<d<4 and e>0):
    total += (d+1)*10
    if(d==3):
        total = (d*10)+20
elif(4<=d<=6 and e>0):
    for i in range(d):
        if(i<4):
            total += i*10
        else:
            total += (i*20)+20
print(total)

    