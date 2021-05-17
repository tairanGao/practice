class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        result = 0
        char_set = set()
        for c in s:
            if c in char_set:
                char_set.remove(c)
                result += 2
            else:
                char_set.add(c)
        if len(char_set) > 0:
            result += 1
        return result
