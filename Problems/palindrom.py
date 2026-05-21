# check given string is palindrome or not "madam" , "level", 


x="level"


# 1st method

if x==x[::-1]:
  print(x[::-1], "it is palindrome")
else:
  print("not a palindrome")  



#2nd method

new_char=''
for char in x:
  new_char=char+new_char

print(new_char)  
  