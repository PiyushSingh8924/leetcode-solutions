class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        adj_list = [[]for _ in range(n+1)]
        indegrees = [0 for _ in range(n+1)]
        dist = [0 for _ in range(n + 1)]
        for u,v in relations:
            adj_list[u].append(v)
            indegrees[v] += 1
        queue = deque()
        for i in range(1,n+1):
            if indegrees[i] == 0:
                queue.append(i)
                dist[i] = time[i - 1]
        while queue:
            curr = queue.popleft()
            for adj_node in adj_list[curr]:
                dist[adj_node] = max(dist[adj_node], dist[curr] + time[adj_node - 1])
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.append(adj_node)
        return max(dist)
    

            

        
