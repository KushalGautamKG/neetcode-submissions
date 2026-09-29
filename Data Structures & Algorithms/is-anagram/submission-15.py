class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for x in s:
            if x not in counts:
                counts[x] = 0
            counts[x] +=1
        countt = {}
        for x in t:
            if x not in countt:
                countt[x] = 0
            countt[x] +=1
        
        
        return sorted(s) == sorted(t)