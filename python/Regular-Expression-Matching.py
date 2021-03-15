class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        # write your code here

        return self.helper(s,p,0,0,{},None)

    def helper(self, s, p, s_i, p_i, visited, previous):
        if (s_i, p_i) in visited:
            return visited[(s_i, p_i)]

        if p_i == len(p) or s_i == len(s):
            return p_i == len(p) and s_i == len(s)
        check = False

        if s[s_i] == p[p_i] or p[p_i] == '.':
            check = self.helper(s, p, s_i + 1, p_i + 1, visited, p[p_i])

        elif p[p_i] == '*':
            n = 0
            while True:
                for i in range(n):
                    if s[s_i + n] == previous or previous == '.':
                        check = self.helper(s, p, s_i + 1, p_i + 1, visited, p[p_i])
                    else:
                        break
                if check:
                    check = True
                    break

                n += 1



        elif s[s_i] != p[p_i]:
            check = False

        visited[(s_i, p_i)] = check
        return check


sol = Solution()
print(sol.isMatch("aaaaaaa", "aaa"))
