class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        # Write your code here
        if n == 1:
            return 0
        dic = [[float('inf')] * n for i in range(n)]

        for i in range(n):
            dic[i][i] = 0

        for i in roads:
            a, b, c = i
            cost = min(c, dic[a - 1][b - 1])
            dic[a - 1][b - 1] = cost
            dic[b - 1][a - 1] = cost

        dp = [float('inf')] * n

        for i in range(n):
            dp[i] = dic[-1][i]

        for i in range(n - 2, -1, -1):
            for j in range(i+1):
                print(i - j)
                for k in range(n):
                    dp[i - j] = min(dic[i][k] + dp[i], dp[i - j])
        print(dp)
        return dp[0]

input = (5, [[1,2,9],[2,3,1],[3,4,9],[4,5,4],[2,4,3],[1,3,2],[5,4,9]])

sol = Solution()
sol.minCost(input[0], input[1])





