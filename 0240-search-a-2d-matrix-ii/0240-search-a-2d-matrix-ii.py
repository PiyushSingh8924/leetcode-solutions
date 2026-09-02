class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0 
        j = cols - 1
        while i <  rows and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True
            elif num > target:
                j -= 1
            else:
                i += 1
        return False
        