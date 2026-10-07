# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        arr = [] 
        def dfs(node, path, remsum):
            if not node:
                return
            if not node.left and not node.right and remsum == node.val:
                arr.append(path + [node.val])
                return
            dfs(node.left, path + [node.val], remsum - node.val)
            dfs(node.right, path + [node.val], remsum - node.val)        
        dfs(root, [], targetSum)
        return arr
