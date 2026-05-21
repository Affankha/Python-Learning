#prime number

x=10  #chek it is prime or not

is_prime= True

for i in range(2, int(x**0.5)+1):
  if(x%i==0):
    is_prime= False
print(is_prime)