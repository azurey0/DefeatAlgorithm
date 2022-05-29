# 1 moves 2 steps, 2 moves 1 step. So when 1 reaches the end, 2 stays in middle
# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while not fast is None and not fast.next is None:
            fast = fast.next.next
            slow = slow.next
        
        return slow
