from collections import deque

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, s):
        # write your code here
        if not s:
            return ""

        s = ''.join(sorted(s))
        visited = {}
        sol = self.asdasd(s, visited)
        return list(sol)

    def asdasd(self, s, visited):
        if s in visited:
            return visited[s]

        if len(s) == 1:
            visited[s] = s
            return s

        temp = set()
        for i in range(len(s)):
            if i!=0 and s[i] == s[i-1]: continue
            s_1 = self.asdasd(s[i], visited)
            s_2_list = self.asdasd(s[0:i]+s[i+1:], visited)
            for s_2 in s_2_list:
                temp.add(s_1+s_2)

        visited[s] = temp
        return temp



s = "aaabbbcccdg"
sol = Solution()
print(sol.stringPermutation2(s))