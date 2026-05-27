from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # Stores elements as [remaining_count, ready_time]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # increment since stored as negative
                if cnt:
                    q.append([cnt, time + n])

            # This should be outside the above if-block
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
