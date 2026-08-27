class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    queue = deque([(r, c)])
                    grid[r][c] = '0'
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            new_i, new_j = x + dx, y + dy
                            if (0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == '1'):
                                grid[new_i][new_j] = '0'
                                queue.append((new_i, new_j))
        return islands