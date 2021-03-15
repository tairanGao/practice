import numpy as np
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        l = len(s)
        dp = [[0] * l for j in range(l)]

        for i in range(l):
            dp[i][i] = 1

        for i in range(l - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
            else:
                dp[i][i + 1] = 1

        for d in range(2, l):
            for i in range(l - d+1):
                j = i + d
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


sol = Solution()
input = "bbkb"
print(sol.longestPalindromeSubseq(input))