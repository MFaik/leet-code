# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        stack = []
        if root:
            stack.append(root)
        
        while len(stack):
            curr = stack.pop()
            ret.append(curr.val)
            for child in curr.children:
                stack.append(child)
        
        return reversed(ret)

# recursive solution
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         ret = []
#         if not root:
#             return ret
#             
#         def dfs(curr: 'Node'):
#             for child in curr.children:
#                 dfs(child)
#             ret.append(curr.val)
#         dfs(root)
#         return ret
