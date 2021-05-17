class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here]


        pl = len(p) + 1
        sl = len(s) + 1
        dp = [[False for _ in range(pl)] for _ in range(sl)]
        dp[0][0] = True

        # only for dealing with when s is empty
        for i in range(1, pl):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i-2]



        # for more general cases
        for i in range(1, sl):
            for j in range(1, pl):
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j - 2] #---完全忽略 （东西+*）combo

                    if s[i - 1] == p[j - 2] or p[j - 2] == '.': # 如果match的上*之前的东西
                        dp[i][j] |= dp[i-1][j]

                else:
                    if s[i-1] == p[j-1] or p[j-1] == ".":
                        dp[i][j] = dp[i-1][j-1]
                print(str((i,j)) + ":" + str(dp[i][j]))

        return dp[-1][-1]




sol = Solution()


s = "aa"
p = "*"
print(sol.isMatch(s,p))