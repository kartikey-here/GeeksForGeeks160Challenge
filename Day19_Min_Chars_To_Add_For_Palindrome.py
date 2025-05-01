#Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.
#Note: A palindrome string is a sequence of characters that reads the same forward and backward.

class Solution:
    def lpsarr(self,p):
        n=len(p)
        lps=[0]*n
        len_lps=0
        i=1
        while i<n:
            if p[i]==p[len_lps]:
                len_lps+=1
                lps[i]=len_lps
                i+=1
            else:
                if len_lps!=0:
                    len_lps=lps[len_lps-1]
                else:
                    lps[i]=0
                    i+=1
        return lps
    def minChar(self, s):
        l=len(s)
        rev=s[::-1]
        s=s+'$'+rev
        lps=self.lpsarr(s)
        return l-lps[-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
