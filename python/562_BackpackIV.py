class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPackIV(self, m, A):
        # write your code here
        if not A or m == 0:
            return 0
        dp = [[0] * (m+1) for _ in range(len(A))]
        for i in range(0, len(A)):
            for j in range(m+1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i - 1][j]
                if j >= A[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - A[i]]
        print(dp)
        return dp[-1][-1]


sol = Solution()
m = 7
A = [1,2,3,7]



print(sol.backPackIV(m,A))