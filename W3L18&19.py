tab = ("java" , "python" ,"swift")
list2=["1","2","3","4","5"]

print("««« Point 1 »»»\n")
print("Method#1 \" pop \"")
list2.pop(3)
print(list2)
print("Method#2 \" insert \"")
list2.insert(3,"0")
print(list2)

print("Method#3 \" index \"")
print(list2.index("3"))

print("Method#4 \" clear \"")
list2.clear()
print(list2)

print("\n------------")

print("\n««« Point 2 »»»\n")

if "python" in tab :
    print("find it ")
else :
    print("didn't")
