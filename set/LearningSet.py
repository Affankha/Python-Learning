# Set is store value in hash formate
# set has fast to search, insert, delete
# stores unique value


s ={1,2,4, "a" ,}
o= {1,"o", "z"}

s.add(20)
s.remove(2)
# s.clear()

print(s)
print(type(s))
print(len(s))

s.clear()

print(s)


#convert other data type into set
y=[1,26,7]
print(type(y))

y=set(y)
print(y)

#union
first={1,23,4,"a"}
second={"a", 5,7,8}
newunion= first.union(second)
print(newunion)

#intersection
interSet=first.intersection(second)
print(interSet)


#Difference
deffSet =first.difference(second)
print(deffSet)