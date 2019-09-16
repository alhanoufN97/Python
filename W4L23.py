T={
    "name": "Alhanouf",
    "Number": 1112,
    "Birthday": "4/4/1997"
    }

if "Birthday" in T :
    print("Birthday is : "+T["Birthday"])

print(len(T))

T["ID"]="SA121"
print(T)

T.pop("Number")
print(T)

T.popitem()
print(T)

del T
print(T)
