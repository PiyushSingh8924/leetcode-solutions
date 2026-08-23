# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def Pathsum(self,node):
        if node is None:
            return 0
        LS = self.Pathsum(node.left)
        if LS < 0:
            LS = 0
        RS = self.Pathsum(node.right)
        if RS < 0:
            RS = 0
        self.maxi = max(self.maxi, LS + RS + node.val )
        return node.val + max(LS,RS)

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = float("-inf")
        self.Pathsum(root)
        return self.maxi