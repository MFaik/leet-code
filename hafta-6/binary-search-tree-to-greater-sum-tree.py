# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getBigger(curr: TreeNode, sum: int) -> int:
            if curr.right:
                sum = getBigger(curr.right, sum)
            sum += curr.val
            curr.val = sum
            if curr.left:
                sum = getBigger(curr.left, sum)
            return sum
        getBigger(root, 0)
        return root
