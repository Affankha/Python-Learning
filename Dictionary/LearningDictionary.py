'''Learnign dictionaries and it's methdos
1 print()
2 perticular element access
3 del perticular element
4 clear() ...delete full dictionary
5 pop()  ...delete specific element
6 popitem()  ..delete from last
7 
'''


x ={"name": "Affan", "age":22, "marid": "no"}
#access perticular element
print(x["name"])

# update any element
x["name"]="khan"
print(x)

#delete any element

del x["marid"]
print(x)


#access each key
for key in x:
  print(key)
  
  
#access all values
for value in x.values():
  print(value)  
  
#accessing key as well as values
for key, value in x.items():
  print(key, value)  
  
#Nested Dictionary
d = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}

print(d["student"]["name"])  