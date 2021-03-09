class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPackIII(self, m, A, V):
        # write your code here
        if not A or m == 0:
            return 0

        dp = [[0] * (m+1) for _ in range(len(A))]
        dp[0][0] = 0
        for i in range(0, len(A)):
            for j in range(m+1):
                dp[i][j] = dp[i - 1][j]
                if A[i] <= j:
                    dp[i][j] = max(dp[i][j], dp[i][j- A[i]] + V[i])

        print(dp)
        return dp[-1][-1]


sol = Solution()
m = 10
A = [2,3,5,7]
V = [1,5,2,4]



print(sol.backPackIII(m,A, V))