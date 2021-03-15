class Solution:

    def threeChains(self, s):
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            for j in range(i):
                if abs(s[j] - s[i]) <= 3:
                    dp[i] += dp[j]
        print(dp)
        return dp[-1]

sol = Solution()
input = [12,15,12]
print(sol.threeChains(input))