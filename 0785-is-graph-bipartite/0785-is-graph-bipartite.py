class Solution(object):
    def dfs(self,node,visited,graph,color):
        visited[node] = color
        for adjnode in graph[node]:
            if visited[adjnode] != -1:
                if visited[adjnode] == color:
                    return False
            else:
                ans = self.dfs(adjnode,visited,graph,1-color)
                if ans == False:
                    return False
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        visited = [-1] * n
        for i in range(0,n):
            if visited[i] == -1:
                ans = self.dfs(i,visited,graph,0)
                if ans == False:
                    return False
        return True
