from typing import List, Dict, Set

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        




        prereq = { c : [] for c in range(numCourses)}


        for crs, pre in prerequisites:


            prereq[crs].append(pre)




        visit = set()
        path = set()


        output = []

        def dfs(crs):

            if crs in path:
                return False

            if crs in visit:
                return True


            
            path.add(crs)

            for nei in prereq[crs]:
                if not dfs(nei):
                    return False


            path.remove(crs)
            visit.add(crs)

            output.append(crs)

            return True


        

        for nei in range(numCourses):
            if not dfs(nei):
                return []


        return output
    
