class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak(self, s, wordSet):

        dp = [False] * (len(s)+1)
        dp[0] = True

        max_length = max([
            len(word)
            for word in wordSet
        ]) if wordSet else 0


        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(i+1, len(s)+1):
                if j - i > max_length:
                    break
                if s[i:j] in wordSet:
                    dp[j] = True

        return dp[-1]

s = "aaaaaaaaaaaaaaaaaaaaaaa"
k = ["a","aa","aaaa"]

wordSet = set()
for i in k:
    wordSet.add(i)

a = Solution()
print(a.wordBreak(s,wordSet))