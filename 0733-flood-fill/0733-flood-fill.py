class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        
        original = image[sr][sc]
        if image[sr][sc] == color:
            return image

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if image[i][j] != original:
                return
            image[i][j] = color
            dfs(i + 1, j)  
            dfs(i - 1, j)  
            dfs(i, j + 1)  
            dfs(i, j - 1) 
        dfs(sr, sc)
        return image