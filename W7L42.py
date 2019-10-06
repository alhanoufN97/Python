class PA :
    def __init__(self , name , age , gender ) :
        self.name = name
        self.age = age
        self.gender=gender

    def Fun (Obj) :
        print (Obj.name , Obj.age , Obj.gender)


P1 = PA("Alhanouf " , 22 , ' F ' )
P1.Fun()

P1.age = 23
P1.Fun()

del P1.age 
P1.Fun()

del P1
P1.Fun()
