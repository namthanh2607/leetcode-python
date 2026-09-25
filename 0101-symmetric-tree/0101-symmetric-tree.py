# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self,p,q):

        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

        return (self.isSymmetricHelper(p.left, q.right) and 
                self.isSymmetricHelper(p.right, q.left))
