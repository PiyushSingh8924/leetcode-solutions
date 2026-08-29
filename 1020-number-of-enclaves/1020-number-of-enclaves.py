class Solution(object):
    def dfs(self, r, c, visited, rows, cols, grid): 
            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return 
            if visited[r][c] == 1: 
                return 
            if grid[r][c] == 0: 
                return 
            visited[r][c] = 1 
            self.dfs(r, c - 1, visited, rows, cols, grid) 
            self.dfs(r - 1, c, visited, rows, cols, grid) 
            self.dfs(r, c + 1, visited, rows, cols, grid) 
            self.dfs(r + 1, c, visited, rows, cols, grid)

    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited =[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    if grid[r][c] == 1: 
                        self.dfs(r, c, visited, rows, cols, grid)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c] == 1:
                    count += 1
        return count