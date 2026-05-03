a=10 
b=20

#swap


'''a,b =b,a
print(a, b)'''

# 2nd method
'''a =a+b
b= a-b

a=a-b

print("a is:", a, "b is:", b)'''

#3rd method xor

a = a^b
b=a^b

print(a)
print(b)

a =b^a
print(a)

# using 4th mehtod
print("using 4th method")
x=12
y=30

def swap(a, b):
    return b,a

x, y=swap(x, y)
print(x, y)


  


