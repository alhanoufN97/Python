class A :
    def __init__(self) :
        self.a= 2

    def __iter__(self) :
        self.a = 2
        return self

    def __next__(self) :
        if self.a <=30 :
            r =self.a
            self.a += 5
            return r
        else :
            raise StopIteration
    



    
Table = ("Python" , "Java" ,"C++")

TAB = iter(Table)


print(next(TAB))
print(next(TAB))
print(next(TAB))

T= "Python"

for x in T :
    print(x)

CL = A()
TA = iter(CL)

for x in TA :
    print(next(TA))
