def Fun1(x) :
    r=1
    for y in x :
        print(y*r)
        r+=1

def Fun2(D) :
    if D <= 10 :
        return True
    else :
        return False

def Fun3(f) :
    if (f<0) :
        res = f+Fun3(f+1)
        print (res)
    else :
        res =0
    return res 
    
    
    
x = [ " java " , "C++ " , " Python "]

Fun1(x)
print(Fun2(9))
print(Fun2(11))
Fun3(-9)
