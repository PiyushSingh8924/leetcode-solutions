class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited =[[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if grid[r][c] == 1:
                        queue.append((r,c))
                        visited[r][c] = 1
        while queue:
            i,j = queue.popleft()
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                dx = i + x
                dy = j + y
                if dx < 0 or dx >= rows or dy < 0 or dy >= cols:
                    continue
                if grid[dx][dy] == 0:
                    continue
                if grid[dx][dy] == 1 and visited[dx][dy] == 1:
                    continue
                queue.append((dx,dy))
                visited[dx][dy] = 1
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1
        return count
