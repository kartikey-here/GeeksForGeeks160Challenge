#Given an array arr[] of n sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list, then return the head of the merged linked list.


'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:
    def mergeKLists(self, arr):
        dummy=Node(None)
        cur=dummy
        q=[(x.data,x,) for x in arr]
        import heapq
        heapq.heapify(q)
        while q:
            ele=heapq.heappop(q)[1]
            if ele:
                cur.next=ele
                if ele.next:
                    heapq.heappush(q,(ele.next.data,ele.next,))
                cur=cur.next
        return dummy.next
        # code here
        # return head of merged list
