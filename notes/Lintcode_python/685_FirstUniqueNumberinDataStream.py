from collections import deque

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        first = -1
        dict = {-1: False}
        queue = deque()
        terminated = False
        for n in nums:
            if n not in dict:
                if first == -1:
                    first = n
                else:
                    queue.append(n)
                dict[n] = True

            else:
                dict[n] = False
                while queue and not dict[first]:
                    first = queue.popleft()
                if not dict[first]:
                    first = -1
            if n == number:
                terminated = True
                break

        if not terminated:
            return -1

        return first


nums = [1, 2, 2, 1, 3,4,3,5, 4]
number =5

sol = Solution()
print(sol.firstUniqueNumber(nums, number))