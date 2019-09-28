def myfunc(n) :
    return lambda a : a * n

F = myfunc(9)
print (F(8))
print (F(' D '))

