class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = [[]for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_list[v].append(u)
            indegrees[u] += 1
        queue = deque()
        for i in range(0,numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        result = []
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adj_node in adj_list[curr_node]:
                indegrees[adj_node] -= 1
                if indegrees[adj_node] == 0:
                    queue.append(adj_node)
        return len(result) == numCourses

