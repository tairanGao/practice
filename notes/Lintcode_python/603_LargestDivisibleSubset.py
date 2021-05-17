from functools import reduce
from math import sqrt
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset

    Given a set of distinct positive integers,
    find the largest subset which has the most elements,
    and every pair of two elements (Si, Sj) in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.


    If there are multiple solutions, return any subset is fine.
    1 \leq len(nums) \leq 500001≤len(nums)≤50000

    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if len(nums) < 2:
            return nums
        nums = sorted(nums)
        solution_index = 0
        max_num = 1
        dp = [1] * len(nums)
        pre = [-1] * len(nums)

        for i in range(len(nums)):
            x = nums[i]
            factors = self.get_facors(x)
            for j in range(i):
                y = nums[j]
                if y not in factors:
                    continue
                if x % y == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j]+ 1
                    pre[i] = j
                    if max_num < dp[i]:
                        max_num = dp[i]
                        solution_index = i

        last = solution_index
        solution = []
        while last != -1:
            solution.append(nums[last])
            last = pre[last]
        return sorted(solution)

    def get_facors(self, n):
        return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)



nums = [1,2,3]

sol = Solution()
print(sorted(sol.largestDivisibleSubset(nums)))