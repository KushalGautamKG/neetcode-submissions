from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        edges = {i : [] for i in range(1, n + 1)}

        for u, v, w in times:
            edges[u].append((v, w))


        time = 0

        visit = {}


        minHeap = [(0, k)]

        heapq.heapify(minHeap)
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue

            visit[n1] = w1
            time = max(time, w1)

            for n2, w2 in edges[n1]:

                if n2 in visit:
                    continue


                heapq.heappush(minHeap, (w1 + w2, n2))


        return time if len(visit) == n else -1
                

