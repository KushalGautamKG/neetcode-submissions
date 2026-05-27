from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # Skip duplicates at the same tree level
                if total + candidates[i] > target:
                    break  # Optimization: no need to go further
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
                prev = candidates[i]
        
        dfs(0, [], 0)
        return res
