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

        queue = deque()
        image[sr][sc] = color
        queue.append((sr,sc))
        while len(queue) > 0 :
            i,j = queue.popleft()
            for dx,dy in ([0,1],[0,-1],[1,0],[-1,0]):
                new_i , new_j = i + dx, j + dy
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if image[new_i][new_j] == original:
                    image[new_i][new_j] = color
                    queue.append((new_i, new_j))
        return image