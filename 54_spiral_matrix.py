class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        top , left = 0,0
        right , bottom = n-1 , m-1
        ans = []
        
        while top <= bottom and left <= right:

            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
        return ans

            
                
