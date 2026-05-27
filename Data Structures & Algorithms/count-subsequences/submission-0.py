class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            # If we've matched all of t, that's a valid subsequence
            if j == len(t):
                return 1

            # If we've run out of s before matching all of t
            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            # If chars match, we can either use this char or skip it
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # Skip this char in s
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)
