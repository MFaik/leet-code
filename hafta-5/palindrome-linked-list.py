# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            fast = fast.next
            slow = slow.next
            if not fast:
                break
            fast = fast.next
        
        #slow is at the mid point rn
        arr = []
        while slow:
            arr.append(slow.val)
            slow = slow.next

        curr = head
        for i in reversed(arr):
            if curr.val != i:
                return False
            curr = curr.next
        return True
