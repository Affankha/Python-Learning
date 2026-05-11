'''GFG
Input: 
N = 5 
names = [john, ala, ilia, sudan, mercy] 
marks = [100, 200, 150, 80, 300]
Output:
ala 200 
ilia 150 
john 100 
mercy 300 
sudan 80'''

dict = {}

N =int(input())
names =input(range(N))
marks =input(range(N))
 
dict ={k:v for k,v in zip(names, marks)}
   
print(dict)