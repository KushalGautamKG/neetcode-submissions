class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        preMap = { i : [] for i in range(n)}




        for p1, p2 in edges:

            preMap[p1].append(p2)
            preMap[p2].append(p1)




        visit = set()


        def dfs(node, prev):


            if node in visit:
                return False


            visit.add(node)


            for nei in preMap[node]:

                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False


            return True


        return dfs(0, -1) and n == len(visit) 



        



