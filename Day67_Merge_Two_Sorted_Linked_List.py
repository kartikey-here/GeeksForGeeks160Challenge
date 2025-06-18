#Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list


'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        list_1 = []
        list_2 = []
        
        while head1:
            list_1.append(head1.data)
            head1 = head1.next
            
        while head2:
            list_2.append(head2.data)
            head2 = head2.next
            
        new_list = list_1 + list_2
        
        new_list.sort()
        
        dummy = Node(new_list[0])
        
        curr = dummy 
        
        for i in range(1,len(new_list)):
            temp = Node(new_list[i])
            curr.next = temp
            curr = curr.next
            
        return dummy
        # code here
