#Given a string s, find the length of the longest substring with all distinct characters. 


#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
    
        i,j=0 ,0
        hashmap = {}
        maximum = 0
        while j < len(s):
            if s[j] not in hashmap:
                hashmap[s[j]] = 1
            elif s[j]  in hashmap:
                hashmap[s[j]] += 1
            if len(hashmap) == j-i+1:
                maximum = max(maximum,j-i+1)
            elif len(hashmap) < j-i+1:
                while(len(hashmap) < j-i+1):
                    hashmap[s[i]] -=1
                    if hashmap[s[i]] == 0:
                        del hashmap[s[i]]
                    i+=1
            j+=1
        return maximum
                
        # code here
