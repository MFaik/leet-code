# https://leetcode.com/problems/binary-tree-postorder-traversal/

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = []
        if root:
            stack.append(root)
        
        while len(stack):
            curr = stack.pop()
            ret.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        ret.reverse()
        return ret

# recursive solution
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ret = []
#         if not root:
#             return ret
#              
#         def dfs(curr: 'Node'):
#             if curr.left:
#                 dfs(curr.left)
#             if curr.right:
#                 dfs(curr.right)
#             ret.append(curr.val)
#         dfs(root)
#         return ret
