''' Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.
 Input: n = 13, m = 4    Output: 12     Explanation: 12 is the closest to 13, divisible by 4.'''
 
n =int(input("enter num n:- "))
m =int(input("enter num m:- "))
 
ans=0

# method 1
ans = (n // m) * m
print("ans: ",ans)


# 2nd method  but it not work for negative num n=-15, m=6
for i in range(n):
  if(i*m>n):
    print((i-1)*m)
    break

