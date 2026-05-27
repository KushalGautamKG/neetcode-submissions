from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list: u -> list of (v, w)
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # (time_so_far, node)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = max(max_time, time)

            for nei, w in edges[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + w, nei))

        return max_time if len(visited) == n else -1
