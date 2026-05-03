n = 4
for i in range(1, n+1):
    print(i)



li = ["coder", "developer", "programmer"]
for x in li:
    print(x)
    
tup =("Salman", "Amer", "Sharuk")
for y in tup:
  print(y)
    
# use of continue (it skips some iteration without breaking loop)    
for letter in 'Salmankhan':
    if letter == 'e' or letter == 's':
        continue
    print(letter, end= '')
print()    # this is only for next lise 


# end=''  This is use for single line o/p   
    
# usf of break (it come out of loop)    
for letter in 'Developer':
    if letter == 'e':
        break
    print(letter, end= '')
    
