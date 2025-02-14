# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        while fast and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return fast

#---naive solution 1---
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         seen = {}
#         curr = head
#
#         while curr:
#             if curr in seen:
#                 return True
#             seen[curr] = True
#             curr = curr.next
#         
#         return False
#---naive solution 2---
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         curr = head
#         cnt = 0
#         while curr and cnt <= 10000:
#             curr = curr.next
#             cnt += 1
#         if cnt > 10000:
#             return True
#         else:
#             return False
