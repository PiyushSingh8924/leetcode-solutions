class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        v = len(graph)
        adj_list = [[]for _ in range(v)]
        indegrees = [0 for _ in range(v)]
        for node in range(v):
            for adj_node in graph[node]:
                adj_list[adj_node].append(node)
        for node in range(len(adj_list)):
            for adj_node in adj_list[node]:
                indegrees[adj_node] += 1
        queue = deque()
        result = []
        for node in range(0,v):
            if indegrees[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            result.append(node)
            for adj_node in adj_list[node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.append(adj_node)
        return sorted(result)

        