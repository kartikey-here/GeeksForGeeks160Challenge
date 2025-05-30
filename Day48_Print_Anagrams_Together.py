#Given an array of strings, return all groups of strings that are anagrams. The strings in each group must be arranged in the order of their appearance in the original array. Refer to the sample case for clarification.

#User function Template for python3


class Solution:
    
    def check(self, s1, s2):
        return sorted(s1) == sorted(s2)
    
    def anagrams(self, arr):
        ans = []
        for i in range(len(arr)):
            if not ans:
                temp = [arr[i]]
                ans.append(temp)
            else:
                added = False
                for j in range(len(ans)):
                    if self.check(ans[j][0], arr[i]):
                        ans[j].append(arr[i])
                        added = True
                    
                if not added:
                    temp = [arr[i]]
                    ans.append(temp)
        return ans
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
