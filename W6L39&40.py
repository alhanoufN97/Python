def fun(x , y) :
    if x > 0 :
        res= y * fun(x-1 , y) 
    else :
        res=1
    return res

print(fun(3 , 5))

L = [-4 , -6 , - 5 , - 1 , 2 , 3 , 7 , 9 , 88 ]
K = lambda a : a > 0
for x in L :
    result = K(x)
    if(result ):
        print(x)

    
