# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(curr: TreeNode):
            if curr.left:
                invert(curr.left)
            if curr.right:
                invert(curr.right)
            curr.left, curr.right = curr.right, curr.left
        if root:
            invert(root)
        return root
