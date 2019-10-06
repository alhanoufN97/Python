class A :
    def __init__(self , Name , Age ) :
        self.name = Name
        self.age = Age
    def Fun1 (Obj) :
         print (Obj.name , Obj.age)

class B(A) :
     def __init__(self , Name , Age , Gender ) :
         super().__init__(Name , Age )
         self.Gender = Gender

     def Fun (Obj) :
         print ("In child class : "+ Obj.name , Obj.age , Obj.Gender)
    
       

P1 = B("Alhanouf " , 22 ,'F')

P1.Fun1()
P1.Fun()
