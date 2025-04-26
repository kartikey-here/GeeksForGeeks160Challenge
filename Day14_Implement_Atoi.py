#Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.
#Cases for atoi() conversion:
#Skip any leading whitespaces.
#Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
#Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
#If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.


#User function template for Python
class Solution:
    def myAtoi(self, s):
        fneg=fnum=0
        s=s.strip()
        x=''
        for i in s:
            if i in ('-','+'):
                fneg+=1
                if fneg>1 or fnum>=1:
                    break
                x+=i
            elif((i) in ('0','1','2','3','4','5','6','7','8','9')):
                fnum+=1
                x+=i
            else:
                break
        if x in('-','+',''):
            return 0
        x=int(x)
        if x>(2**31)-1:
            return (2**31)-1
        if x<(2**31)*-1:
            return (2**31)*-1
        return x
                


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends
