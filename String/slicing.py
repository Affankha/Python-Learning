# slicing String == cut some part of String

x="action and reaction are eqaul and opposite"

print(len(x))
print(x[3:15])
print(x[:3])
print(x[1:])


# String are immutable we cannot change string 

x= 'AFFAN KHAN'
y='Student '
x = "Tu"+ x[1:]
print(x)

print(x.lower())


#strinp remove leading and trealing spacess
z="    Rantan tata is a owner of TATA Group"
print(z)
print(z.strip())


#replace() 

print(z.replace('TATA', 'GIO'))

#concatnet
print(z+ " " +x)

#Repeat String
print(y * 2)

#formating string
print(f"Name: {x}, Biradary: {y}")

#another way of string formating
sentence = "i am working at {} from {}".format("Tcs", "22 Dec")

print(sentence)