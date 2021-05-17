class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        max_len = 0
        i = 0
        output = ""

        if len(s)<= 1:
            return s

        while i < len(s):
            current_len = 0
            i += 0.5
            if i % 1 == 0:
                current_len += 1
                left = int(i - 1)
                right = int(i + 1)
            else:
                left = int(i)
                right = left + 1

            j = 0
            while left - j >= 0 and right +j <len(s):
                if s[left - j] == s[right +j]:
                    current_len += 2
                    if current_len > max_len:
                        output = s[left - j:right + j+1]
                        max_len = current_len
                    j += 1
                else:
                    break


        return output


input = "a"

sol = Solution()
print(sol.longestPalindrome(input))