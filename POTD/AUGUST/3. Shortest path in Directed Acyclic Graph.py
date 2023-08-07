#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        dist = [float('inf')] * n
        dist[0] = 0

        for i in range(n - 1):
            for edge in edges:
                u, v, weight = edge
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist