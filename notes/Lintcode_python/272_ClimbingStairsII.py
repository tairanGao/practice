class Solution:
    """
    @param n: An integer
    @return: An Integer
    """

    def climbStairs2(self, n):
        # write your code here
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(n+1):
            for steps in [1, 2, 3]:
                if i - steps >= 0:
                    dp[i] += dp[i - steps]
                else:
                    break

        return dp[n]



sol = Solution()
print(sol.climbStairs2(3))