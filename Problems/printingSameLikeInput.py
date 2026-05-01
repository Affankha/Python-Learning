# a=4, b=3, c=&     o/p = 4444&3333


a = int(input())
b = int(input())
c=input()

ans=[]

for i in range(a):
   if i<a:
     ans.append(a)
ans.append(c)



for j in range(b):
  if j<b:
    ans.append(b)

print(list(ans))