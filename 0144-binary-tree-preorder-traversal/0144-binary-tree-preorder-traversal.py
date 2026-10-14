# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        
        self.ret = [root.val]
        self.help_preorder(root)
        return self.ret
    
    def help_preorder(self, node):
        if node.left:
            self.ret.append(node.left.val)
            self.help_preorder(node.left)
        if node.right:
            self.ret.append(node.right.val)
            self.help_preorder(node.right)
         