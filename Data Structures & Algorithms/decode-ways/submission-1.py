class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        one_ahead = 1   # dp[i+1], dp[n] = 1
        two_ahead = 1   # dp[i+2], seed with dp[n]
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = one_ahead
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                    cur += two_ahead
            two_ahead, one_ahead = one_ahead, cur
        return one_ahead

        