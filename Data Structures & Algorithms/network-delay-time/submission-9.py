class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))



        minHeap = [(0, k)]
        time = 0

        shortest = {}

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1] = t1
            time = max(t1, time)

            for n2, t2 in edges[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (t1 + t2, n2))

        return time if len(shortest) == n else -1