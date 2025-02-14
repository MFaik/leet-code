# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        if not head_a or not head_b:
            return
        
        a_len = 1
        curr_a = head_a
        while curr_a.next:
            a_len += 1
            curr_a = curr_a.next
        # curr_a is the last node in the list
        
        b_len = 1 
        curr_b = head_b
        while curr_b.next:
            b_len += 1
            curr_b = curr_b.next
        # curr_b is the last node in the list

        for i in range(a_len-b_len):
            head_a = head_a.next
        for i in range(b_len-a_len):
            head_b = head_b.next
        while head_a != head_b:
            head_a = head_a.next
            head_b = head_b.next
        
        return head_a
