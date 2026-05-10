#print squares of list element

a=[2,3,4,5,6,7,8,9,10]

squares =[val**2 for val in a]
print(squares)

#check value is even or odd

b =[1,23,5,6,7,86,8,0]
res=[val for val  in b if val%2==0]
print("even numbers are: ", res)