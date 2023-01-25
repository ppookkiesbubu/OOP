def myfunc(n):
    return lambda a : a * n

d = myfunc(2)
t = myfunc(3)
print(d(11))
print(t(12))