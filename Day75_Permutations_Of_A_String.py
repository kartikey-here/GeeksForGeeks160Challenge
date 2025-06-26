#Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.


##User function Template for python3

class Solution:
    def findPermutation(self, s):
        def solve(s, ind, ans):
            if ind == len(s):
                ans.append(''.join(s))
                return
            seen = set()
            for i in range(ind, len(s)):
                if s[i] in seen:
                    continue  # skip duplicate characters at this position
                seen.add(s[i])
                s[ind], s[i] = s[i], s[ind]
                solve(s, ind + 1, ans)
                s[ind], s[i] = s[i], s[ind]  # backtrack

        chars = list(s)
        ans = []
        solve(chars, 0, ans)
        return ans


        # Code here
        
