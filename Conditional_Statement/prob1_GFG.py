'''There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false

Example 1:
          Input:
          j_angry = True, s_angry = True
          Output:
          True '''
          
          
j_angry =input("enter j is angry: ")
s_angry=input("enter s is angry: " )

if j_angry == s_angry:
    print( True)
else:
    print( False)
