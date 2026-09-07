class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for s in strs:

            let = [0] * 26
            for c in s:

                let[ord(c) - ord('a')] += 1


            res[tuple(let)].append(s)


        return list(res.values())

            


