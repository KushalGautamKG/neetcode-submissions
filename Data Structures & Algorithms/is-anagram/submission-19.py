class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for x in s:
            if x not in countS:
                countS[x] = 0
            countS[x] += 1

        for z in t:
            if z not in countT:
                countT[z] = 0
            countT[z] +=1

        return countS == countT
            



        