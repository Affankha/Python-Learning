# reverse the string using different methods

x=["a", "b", "c"]

# print(x[::-1])      #using slicing


#2nd way

new_string =''

for char in x:
  new_string= char + new_string
  
print(new_string)
