class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dist = abs(x2 - x1) + abs(y2 - y1) 
                adj[i].append([dist, j])

                adj[j].append([dist, i])


        res = 0

        visit = set()

        minHeap = [[0, 0]]

        n = len(points)
        while len(visit) < n:

            dist, i = heapq.heappop(minHeap)

            if i in visit:
                continue


            res += dist
            visit.add(i)
            for dist2, j in adj[i]:
                if j not in visit:
                    

                    heapq.heappush(minHeap, [dist2, j])




        return res



            

            





        


            