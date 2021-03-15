class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i+1] = True

            else:
                for j in range(i+1):
                    if dp[j] and s[j:i+1] in wordDict:
                        dp[i+1] = True
        return dp[-1]


sol = Solution()
s = "applepenapple"
wordDict =  ["apple", "pen"]

print(sol.wordBreak(s,wordDict))