# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def solve(self,node):
        if node is None:
            return 0
        LH = self.solve(node.left)
        if LH == -1:
            return -1
        RH = self.solve(node.right)
        if RH == -1:
            return -1
        if abs(RH -LH) > 1:
            return -1
        return 1 + max(LH,RH)
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        x = self.solve(root)
        if x == -1:
            return False
        return True