class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here

        dict = {0:-1}
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp in dict:
                return [dict[temp]+1, i]
            dict[temp] = i

        return [-1,-1]


nums =  [-3, 1, 2, -3, 4]

sol = Solution()
print(sol.subarraySum(nums))