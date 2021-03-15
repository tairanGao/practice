class Solution_DFS:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        return self.helper(s,p,0,0,{})

    def helper(self, s, p, si, pi, visited):

        if (si,pi) in visited:
            return visited[(si,pi)]

        if s[si:] == p[pi:] == '':
            return True
        if p[pi:] == '':
            return False

        if p[pi] == "*":
            for i in range((len(s)-si+1)):
                if self.helper(s, p, si + i, pi + 1,visited):
                    visited[(si, pi)] = True
                    return True
            visited[(si, pi)] = False
            return False

        if s[si:] == '':
            return False

        if p[pi] == "?" or p[pi] == s[si]:
            result = self.helper(s,p,si+1,pi+1,visited)
            visited[(si, pi)] = result
            return result

        if p[pi] != s[si]:
            visited[(si, pi)] = False
            return False

        return False


class Solution_DP:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        n_s = len(s)
        n_p = len(p)
        dp = [[False for i in range(n_s+1)] for j in range(n_p+1)]

        si = 0
        pi = 0
        dp[pi][si] =
        while pi < n_p:
            if dp[pi][si] is not None and not dp[pi][si]:
                break
            if p[pi] == "*":
                for i in range(pi,n_s):
                    pass
            if p[pi] == "?" or p[pi] == s[si]:
                dp[pi][si] = True
                pi += 1
                si += 1
            if p[pi] != s[si]:
                dp[pi][si] = False
                break






    def helper(self, s, p, si, pi, visited):

        if (si,pi) in visited:
            return visited[(si,pi)]

        if s[si:] == p[pi:] == '':
            return True
        if p[pi:] == '':
            return False

        if p[pi] == "*":
            for i in range((len(s)-si+1)):
                if self.helper(s, p, si + i, pi + 1,visited):
                    visited[(si, pi)] = True
                    return True
            visited[(si, pi)] = False
            return False

        if s[si:] == '':
            return False

        if p[pi] == "?" or p[pi] == s[si]:
            result = self.helper(s,p,si+1,pi+1,visited)
            visited[(si, pi)] = result
            return result

        if p[pi] != s[si]:
            visited[(si, pi)] = False
            return False

        return False









sol = Solution_DP()
s = "aas"
p = "?aasdasd"

print(sol.isMatch(s,p))









