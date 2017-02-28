# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        return self.reverse(head)
        
    def reverse(self,head, prev = None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        return self.reverse(n, head)
            