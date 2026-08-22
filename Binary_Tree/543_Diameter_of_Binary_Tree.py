class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0

        def height(node):
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter,left_height +right_height )
            return 1 + max(left_height,right_height)

        height(root)
        return self.diameter
        