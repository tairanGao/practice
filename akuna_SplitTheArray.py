import math
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def split_the_array(self, vals):
        # Right pointer

        n = len(vals)
        dp = [0] * (n+1)
        dp[-1] = 0

        for i in range(n-1, -1, -1):
            dp[i] = 1 +dp[i+1]
            for j in range(i+1, n):
                if math.gcd(vals[i], vals[j]) > 1:
                    dp[i] = min(dp[i], 1+dp[j+1])

        return dp[0]


sol = Solution()
vals = [2,3,2,2,3,3,9,9,5]
print(sol.split_the_array(vals))
