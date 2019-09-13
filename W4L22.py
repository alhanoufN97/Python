T={
    "name": "Alhanouf",
    "Number": 1112,
    "Birthday": "4/4/1997"
    }
print(T)

f= T["Number"]
print(f)

for x in T :
    print(x)
    
for x in T.values() :
    print(x)
T["Number"]=4449

for x , y in T.items() :
    print(x , y)
