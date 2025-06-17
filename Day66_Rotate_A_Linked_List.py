#Given the head of a singly linked list, your task is to left rotate the linked list k times.



class Solution:
    def rotate(self, curr, k):
        # code here
        _head = head
        _tail = _head
        count = 1
        while _tail.next:
            _tail = _tail.next
            count += 1
        k = k % count
        for _ in range(k):
            tmp = _head
            if _head.next:
                _head = _head.next
                tmp.next = None
                _tail.next = tmp
                _tail = _tail.next

        return _head

