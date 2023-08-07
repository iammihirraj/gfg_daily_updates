#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        def dfs_helper(v, visited, result):
            visited[v] = True
            result.append(v)
            for u in adj[v]:
                if not visited[u]:
                    dfs_helper(u, visited, result)

        visited = [False] * V
        result = []
        dfs_helper(0, visited, result)
        return result