class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        freqMap = defaultdict(int)

        res = [[] for i in range(len(nums) + 1)]
        res2 = []
        for n in nums:

            freqMap[n] += 1
        

        for n, c in freqMap.items():
            res[c].append(n)


        for i in range(len(res) - 1, 0, -1):
            

            for n in res[i]:
                res2.append(n)

                if len(res2) == k:
                    return res2

