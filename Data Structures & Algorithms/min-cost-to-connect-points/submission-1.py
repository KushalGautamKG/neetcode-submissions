from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}  # i -> list of (cost, neighbor)

        # Build an undirected complete graph with Manhattan distances
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))  # <-- fix: add reverse edge

        res = 0
        visited = set()
        minH = [(0, 0)]  # (cost, node)

        while len(visited) < n:
            cost, u = heapq.heappop(minH)
            if u in visited:
                continue
            visited.add(u)
            res += cost
            for w, v in adj[u]:
                if v not in visited:
                    heapq.heappush(minH, (w, v))

        return res
