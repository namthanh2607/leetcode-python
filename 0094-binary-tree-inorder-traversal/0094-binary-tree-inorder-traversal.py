# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        k = root
        def IOT(k):
            if k == None:
                return 
            if k.left:
                IOT(k.left)
            ans.append(k.val)

            if k.right:
                IOT(k.right)

        IOT(root)
        return ans

            

        
        



        