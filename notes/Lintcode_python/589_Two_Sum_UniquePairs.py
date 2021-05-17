
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) <= 1:
            return 0
        used = {}
        num = 0
        for each in nums:
            if target - each in used and used[target - each] == 0:
                num += 1
                used[target - each] = 1
                used[each] = 1
            if each not in used:
                used[each] = 0
        return num

nums = [11,11,11,1,2,3,4]

target = 22

sol = Solution()
print(sol.twoSum6(nums, target))