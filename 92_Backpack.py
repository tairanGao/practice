class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        if not A or m == 0:
            return 0

        dp = [[0] * (m+1) for _ in range(len(A))]
        dp[0][0] = 0
        for i in range(0, len(A)):
            for j in range(m+1):
                if A[i] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j- A[i]] + A[i])
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp)
        return dp[-1][-1]


sol = Solution()
m = 10
A = [3,3,5,2]



print(sol.backPack(m,A))