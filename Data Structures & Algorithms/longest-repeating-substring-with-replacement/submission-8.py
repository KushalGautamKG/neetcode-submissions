class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l = 0

        maxF = 0

        longest = 0

        dic = defaultdict(int)



        for r in range(len(s)):

            
            dic[s[r]] += 1

            maxF = max(maxF, dic[s[r]])
            while (r - l + 1) - maxF > k:

                


                dic[s[l]] -= 1
                l += 1


            

            longest = max(r - l + 1, longest)

        return longest




