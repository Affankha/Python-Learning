# find the Sum of N Natural no's

n =int(input("enter n natural no.:"))


sumNnaturalNum = int(n*(n+1)/2)

print("The sum of n natural no. is", sumNnaturalNum)


#2nd Method

z=int(input())
summation =0
for i in range(1, z+1):
  summation += i

print("the some of", z, "Natural nombe is", summation)

