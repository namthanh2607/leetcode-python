# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.help(root)

    def help(self,u):
        if not u:
            return 0
        if not u.left and not u.right:
            return 1
        elif u.left and u.right:
            return max(self.help(u.left), self.help(u.right)) + 1
        elif u.left:
            return self.help(u.left) + 1
        elif u.right:
            return self.help(u.right) + 1

        
        
        