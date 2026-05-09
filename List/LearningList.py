#all methods in List

a=[1,2,3,4,5,6]
fruits=['apple', 'banana', 'coconut', 'mango']

#list print
print(a)

#next line print
for item in fruits:
  print(item)
  
# print specific element 
print(a[0])

#change value
a[0]=90
print(a)

#clear List
    # a.clear()
    # print(a)


#del perticular element

del fruits[2]
print(fruits[2])

#remove an element
a.remove(5)   # it removes value
print(a)

#pop remove element from back or from specific index
a.pop()
print(a)

a.reverse()
print(a)

#nested list

b=[[3,5], [5,6], 10]
print(b[2])
print(b)
print(b[0][0])   #matrix oth row oth col   element