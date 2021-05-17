class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        steps = [(1,2), (-1, 2), (2, 1), (-2, 1)]
        dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
        if grid[0][0] == 1:
            return -1

        dp[0][0] = 0

        row = len(grid)
        col = len(grid[0])

        for j in range(col):
            for i in range(row):
                if grid[i][j] == 1:
                    continue
                for d in steps:
                    x = i + d[0]
                    y = j + d[1]
                    if 0<= x <row and 0 <= y<col :
                        if grid[x][y] == 1 or dp[i][j] == -1:
                            continue
                        if dp[x][y] == -1:
                            dp[x][y] = dp[i][j] + 1
                        else:
                            dp[x][y] = min(dp[x][y], dp[i][j] + 1)

        return dp[-1][-1]

grid =[[0,1,0],[0,0,1],[0,0,0]]

sol = Solution()
print(sol.shortestPath2(grid))