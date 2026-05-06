s =input("enter Roman num: ")

res = 0
roman = {
         'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000
        }

for ch in reversed(s):
        if roman[ch]< prev:
            res-=roman[ch]
        else:
            res+=roman[ch]
        
        prev=roman[ch]
print(res)