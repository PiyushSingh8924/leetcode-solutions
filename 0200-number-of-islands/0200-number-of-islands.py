class Solution(object):
    def bfs(self,i,j,visited,grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((i,j))
        while queue:
            x,y = queue.popleft()
            for xx,yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                dx = x + xx
                dy = y + yy
                if dx < 0 or dy < 0 or dx >= rows or dy >= cols:
                    continue
                if grid[dx][dy] == "0":
                    continue
                if visited[dx][dy] == 1:
                    continue
                visited[dx][dy] = 1
                queue.append((dx,dy))

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
                    self.bfs(r,c,visited,grid)
        return count

                
    