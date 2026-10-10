# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid + 1:])
        return root