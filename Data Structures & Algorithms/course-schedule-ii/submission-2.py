from typing import List, Dict, Set

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency: course -> list of its prerequisites
        prereq: Dict[int, List[int]] = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output: List[int] = []
        visit: Set[int] = set()   # permanently processed (no cycle via this node)
        cycle: Set[int] = set()   # nodes in current DFS path

        def dfs(crs: int) -> bool:
            if crs in cycle:      # found a back-edge => cycle
                return False
            if crs in visit:      # already processed successfully
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            visit.add(crs)
            output.append(crs)    # postorder: prerequisites come first
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []         # cycle detected: no valid ordering

        return output             # <-- move this OUT of the loop

        

        
