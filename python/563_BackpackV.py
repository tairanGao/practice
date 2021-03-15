class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPackV(self, target, nums):
        # write your code here
        if not nums or target == 0:
            return 0
        dp_1 = [0] * (target + 1)
        dp_1[0] = 1

        for i in nums:
            dp_2 = [0] * (target + 1)
            dp_2[0] = 1

            for j in range(len(dp_2)):
                dp_2[j] = dp_1[j]
                if i <= j:
                    dp_2[j] += dp_1[j-i]
            dp_1 = dp_2[:]
        return dp_2[-1]


sol = Solution()
m = 7
A = [1,2,3,3,7]



print(sol.backPackV(m,A))