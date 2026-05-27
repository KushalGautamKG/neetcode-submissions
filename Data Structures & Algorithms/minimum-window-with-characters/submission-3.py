class Solution:
    def minWindow(self, s: str, t: str) -> str:
        


        if not t:
            return ""


        countW, countT = {}, {}
        res = [-1, -1]
        resLen = float("infinity")

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        l = 0
        have, need = 0, len(countT)


        for r in range(len(s)):

            c = s[r]

            countW[c] = countW.get(c, 0) + 1

            if c in countT and countW[c] == countT[c]:
                have += 1


            while have == need:
                countW[s[l]] -= 1
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l : r + 1] if resLen != float("infinity") else ""