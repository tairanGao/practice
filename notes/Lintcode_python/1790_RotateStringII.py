class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        i = (left - right) % len(str)
        return str[i:] + str[:i]




input = "abcdefg"

sol = Solution()
print(sol.RotateString2(input, 5, 2))