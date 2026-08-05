class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = (stone_sum + 1) // 2

        dp = {}

        def dfs(i, total):
            # We have made a decision for every stone
            if i == len(stones):
                return abs(total - (stone_sum - total))

            if (i, total) in dp:
                return dp[(i, total)]

            # Do not place stones[i] in this subset
            skip = dfs(i + 1, total)

            # Place stones[i] in this subset
            take = dfs(i + 1, total + stones[i])

            dp[(i, total)] = min(skip, take)
            return dp[(i, total)]

        return dfs(0, 0)