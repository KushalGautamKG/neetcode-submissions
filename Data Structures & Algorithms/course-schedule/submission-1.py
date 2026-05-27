class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()  # nodes in current DFS stack

        def dfs(crs: int) -> bool:
            if crs in visiting:       # found a cycle
                return False
            if not preMap[crs]:       # no prereqs left -> good
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            preMap[crs] = []          # memoize: this course is resolvable
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        