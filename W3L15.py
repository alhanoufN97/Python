List1 =['A' ,'B' , 'C' , 'D']

Clist = List1.copy()
print(Clist)

Slist =List1
List1.append('FF')
List1.remove('B')
List1.pop()
List1.pop(1)
List1.insert(4,'XX')
print(List1)
print(Clist) # use method copy
print(Slist) # make equal 
print(len(List1))
