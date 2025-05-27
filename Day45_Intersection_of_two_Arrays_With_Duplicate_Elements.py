#Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not have duplicate elements and the result should contain items in any order.

#Note: The driver code will sort the resulting array in increasing order before printing.



class Solution:
    def intersectionWithDuplicates(self, a, b):
        a=set(a)
        b=set(b)
        return list(a.intersection(b))
        # code here
