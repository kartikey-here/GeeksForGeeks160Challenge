#Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).

#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        if b==1 and e==0:
            return 1
    
        elif b==0:
            return 0
        
        elif e==1:
            return b
        
        else:
               return pow(b,e)
        print(power())
        # Code Here
