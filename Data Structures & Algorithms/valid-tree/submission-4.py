class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True


        premap = {i : [] for i in range(n)}


        for n1, n2 in edges:
            premap[n1].append(n2)

            premap[n2].append(n1)


        
        visit = set()

        def dfs(node, prev):

            if node in visit:
                return False

            

            visit.add(node)

            for nei in premap[node]:

                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False


            return True


        return dfs(0, -1) and len(visit) == n



                

