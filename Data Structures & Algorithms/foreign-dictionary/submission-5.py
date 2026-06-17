class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        graph = { c : set() for w in words for c in w }


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]


            minLen = min(len(w1), len(w2))

            if w1[ : minLen] == w2[ : minLen]:
                if len(w1) > len(w2):
                    return ""



            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])

                    break

        visited = {}


        res = []


        def dfs(c):

            if c in visited:
                return visited[c]


            visited[c] = True

            for nei in graph[c]:
                if dfs(nei):
                    return True


            visited[c] = False
            res.append(c)

            return visited[c]


        for char in graph:
            if dfs(char):
                return ""

        res.reverse()

        return "".join(res)



