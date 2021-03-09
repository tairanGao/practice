class Solution:
    """
    @param amount: a total amount of money amount
    @param coins: the denomination of each coin
    @return: the number of combinations that make up the amount
    """

    def change(self, amount, coins):
        # write your code here
        if amount <= 0 or not coins:
            return 0

        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            if 0 <= dp[i]:
                for c in coins:
                    if i + c <= amount:
                        dp[i + c] = min(dp[i] + 1, dp[i + c]) if dp[i + c] > 0 else dp[i] + 1
        print (dp)

        return 1



sol = Solution()
amount = 8
coins = [2, 3, 8]


print(sol.change(amount,coins))