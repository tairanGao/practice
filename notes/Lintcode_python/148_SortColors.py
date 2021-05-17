class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing

    使用一次扫描的办法。 设立三根指针，left, index, right。定义如下规则：
    left 的左侧都是 0（不含 left）
    right 的右侧都是 2（不含 right）
    index 从左到右扫描每个数，如果碰到 0 就丢给 left，碰到 2 就丢给 right。碰到 1 就跳过不管。

    """
    def sortColors(self, nums):
        # write your code here
        left, i, right = 0, 0, len(nums) - 1

        while i < right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

        return nums






