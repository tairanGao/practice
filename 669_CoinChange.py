class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount, v):
        # write your code here
        if not coins:
            return -1
        max_val = float('inf')
        dp = [max_val] * (amount+1)
        dp[0] = 0

        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        print(dp)
        return dp[-1] if dp[-1] <= v else -1


sol = Solution()
amount = 55
coins = [5,10]
k = 6

print(sol.coinChange(coins,amount, k))