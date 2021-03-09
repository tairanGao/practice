# coding=utf-8
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict_):
        # Write your code here
        list_words = list(dict_)
        for i in range(len(list_words)):
            list_words[i] = list_words[i].lower()

        return self.helper(s.lower(), set(list_words), {})

    def helper(self, s, dict_,visited):
        print(visited)
        if not s or not dict_ or s == "":
            return 0
        count = 0
        if s in visited:
            return visited[s]
        for i in range(1, len(s) + 1):
            if s[0:i] in dict_:
                if i == len(s):
                    visited[s] = 1 + count
                    return 1 + count
                count += self.helper(s[i:], dict_,visited)
        visited[s] = count
        return count


class Solution2:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0

        # 将字符全部转化为小写，并将dict转换成hash_stet存储，降低判断子串存在性的时间复杂度
        n, hs = len(s), set()
        s = s.lower()
        for d in dict:
            hs.add(d.lower())

        # dp[i]表示s[0:i](不含s[i])的拆分方法数
        dp = [0 for _ in range(n + 1)]
        # dp[0]表示空串的拆分方法数
        dp[0] = 1

        for i in range(n):
            for j in range(i, n):
                # 若存在匹配，则进行状态转移
                if s[i:j + 1] in hs:
                    dp[j + 1] += dp[i]

        return dp[n]

s = "Catmat"
k = ["Cat","mat","Ca","tm","at","C","Dog","og","Do"]
dict_ = set()

for i in k:
    dict_.add(i)

a = Solution2()
print(a.wordBreak3(s,dict_))