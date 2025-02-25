# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangeSum(curr: TreeNode) -> int:
            sum = 0
            if curr.val >= low and curr.val <= high:
                sum = curr.val
            if curr.val >= low and curr.left:
                sum += rangeSum(curr.left)
            if curr.val <= high and curr.right:
                sum += rangeSum(curr.right)
            return sum
        return rangeSum(root)
