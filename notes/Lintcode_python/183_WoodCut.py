class Solution:
    """


    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or k == 0:
            return 0
        left = 1
        right = max(L)

        left_num = sum([i//left for i in L])
        if k > left_num:
            return 0


        while left + 1 < right:
            mid = (left + right)//2
            mid_num = sum([i//mid for i in L])
            if mid_num >= k:
                left = mid
            else:
                right = mid

        left_num = sum([i//left for i in L])
        right_num = sum([i//right for i in L])
        if right_num >= k:
            return right
        if left_num >= k:
            return left


        return 0


L = [232, 124, 456]
k = 7

sol = Solution()
print(sol.woodCut(L,k))