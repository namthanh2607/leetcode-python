# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.ret = []
        self.help(root,root.val)
        return sum(self.ret)

    def help(self, node, cur):
        if not node.left and not node.right:
            return self.ret.append(cur)
        
        if node.left:
            self.help(node.left, cur * 10 + node.left.val)

        if node.right:
            self.help(node.right, cur * 10 + node.right.val)