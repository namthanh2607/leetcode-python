# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        start = root
        def back(start):
            if start.left:
                ans.append('->') 
                ans.append(str(start.left.val))
                back(start.left)
                ans.pop()
                ans.pop()
            if start.right:
                ans.append('->') 
                ans.append(str(start.right.val))
                back(start.right)
                ans.pop()
                ans.pop()

            elif not start.left and not start.right:
                ret.append(''.join(ans))

        ans = [str(start.val)]
        back(start)
        return ret