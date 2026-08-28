class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        dist = [[-1] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        while len(queue) > 0:
            i , j = queue.popleft()
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_i = dx + i
                new_y = dy + j
                if 0 <= new_i < rows and 0 <= new_y < cols and dist[new_i][new_y] == -1:
                    dist[new_i][new_y] = dist[i][j] + 1
                    queue.append((new_i,new_y))
        return dist