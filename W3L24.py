student1 = {
    "name": "Alhanouf",
    "Number": 1112,
    "Birthday": "4/4/1997"
    }
student2 = {
    "name": "Nora",
    "Number": 1132,
    "Birthday": "4/5/1999"
    }
student3 = {
    "name": "Sara",
    "Number": 2334,
    "Birthday": "5/8/1997"
    }
    
School = { "student1":student1 , "student2":student1 ,"student3" :student3}
print(School)

print("\n\n------All Student-----")
student4 = dict(name="Lama" ,Number = 43531 , Birthday="17/3/1996")
School["student4"]=student4
print(School)
