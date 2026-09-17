class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        


        time = 0

        q = deque()

        counter = Counter(tasks)

        minHeap = [-i for c, i in counter.items()]


        heapq.heapify(minHeap)


        while minHeap or q:
            time += 1
            
            if minHeap:
                freq = heapq.heappop(minHeap) + 1
                if freq != 0:
                    q.append((time + n, freq))

            if q and time == q[0][0]:
                time, freq = q.popleft()

                heapq.heappush(minHeap, freq)



        return time







