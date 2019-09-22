def Fun1(x = 5) :
    x*=x
    Fun2(x)

def Fun2(x) :
    print(x)

x= input("input int Num : ")
x=int(x)
Fun1(x)


x= input("input int Num : ")
x=int(x)
Fun1(x)


print("other call funcation ")
Fun1()
