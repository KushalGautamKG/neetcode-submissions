class Solution:
    def minWindow(self, s: str, t: str) -> str:
        


        if not t:
            return ""


        tMap = defaultdict(int)


        window = defaultdict(int)



        for c in t:
            tMap[c] += 1


        need = len(tMap)



        resLen = float("infinity")
        res = [-1, -1]


        l = 0 
        have = 0


        for r in range(len(s)):

            window[s[r]] += 1

            if s[r] in tMap and window[s[r]] == tMap[s[r]]:
                have += 1


            while have == need:

                if (r - l + 1) < resLen:
                    resLen = r - l + 1

                    res = [l, r]


                window[s[l]] -= 1


                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1

                l += 1

        l, r = res
    
        return s[l : r + 1] if resLen != float("infinity") else ""