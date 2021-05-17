class Solution:
    """
    Find any position of a target number in a sorted array. Return -1 if target does not exist.
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        if target < nums[0] or target > nums[-1]:
            return -1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid
            else:
                right = mid

        if target == nums[right]:
            return right
        if target == nums[left]:
            return left
        return -1

nums = [1,2]
target = 2

sol = Solution()
print(sol.findPosition(nums, target))