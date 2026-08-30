class Solution(object):
    def dfs(self,i,j,visited,grid):
        rows = len(grid)
        cols = len(grid[0])
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return
        if visited[i][j] == 1:
            return
        if grid[i][j] == "0":
            return
        visited[i][j] = 1
        self.dfs(i+1,j,visited,grid)
        self.dfs(i-1,j,visited,grid) 
        self.dfs(i,j+1,visited,grid) 
        self.dfs(i,j-1,visited,grid) 

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)]for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] ==0:
                    count += 1
                    self.dfs(r,c,visited,grid)
        return count

                
    