#You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.
#Note: The characters in the strings are in lowercase.

#User function Template for python3

class Solution:
    def lpsarr(self,p):
        n=len(p)
        lps=[0]*n
        plen=0
        lps[0]=0
        i=1
        while i<n:
            if p[i]==p[plen]:
                plen+=1
                lps[i]=plen
                i+=1
            else:
                if plen!=0:
                    plen=lps[plen-1]
                else:
                    lps[i]=0
                    i+=1
        return lps
    def areRotations(self,s1,s2):
        #code here
        t=s1+s1
        p=s2
        n=len(t)
        m=len(p)
        lps=self.lpsarr(p)
        i=0
        j=0
        while i<n:
            if p[j]==t[i]:
                j+=1
                i+=1
            if j==m:
                return True
            elif i<n and p[j]!=t[i]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return False





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (Solution().areRotations(s1, s2)):
            print("true")
        else:
            print("false")

# } Driver Code Ends
