class A :
    def __init__(self , Name , Age ) :
        self.name = Name
        self.age = Age

class B(A) :
     def __init__(self , Name , Age , Gender ) :
         A.__init__(self , Name , Age )
         self.Gender = Gender

     def Fun (Obj) :
         print (Obj.name , Obj.age , Obj.Gender)
    
       

P1 = B("Alhanouf " , 22 , ' F ' )

P1.Fun()
