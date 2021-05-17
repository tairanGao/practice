class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, targer):
        # write your code here
        if not A:
            return [[]]
        A = sorted(A)
        sol = []
        self.dfs(A, k, targer, sol, [])
        return sol


    def dfs(self, A, k, target, sol, curr_sol):
        if target == 0 and k ==0:
            sol.append(curr_sol)
            return
        if k == 0 or len(A) == 0:
            return

        for i in range(len(A)):
            curr_sol.append(A[i])
            self.dfs(A[i+1:], k-1, target-A[i], sol, curr_sol.copy())
            curr_sol.pop()
        return


A = [1,3,4,6]
k = 3
target = 8

sol = Solution()
print(sol.kSumII(A, k, target))