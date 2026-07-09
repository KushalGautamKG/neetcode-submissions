class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        


        intervals.sort()
        res = 0


        end = intervals[0][1]

        for i in range(1, len(intervals)):

            start = intervals[i][0]


            if start >= end:
                end = intervals[i][1]


            else:
                res += 1

                end = min(end, intervals[i][1])


        return res