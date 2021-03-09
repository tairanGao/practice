class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def letterCombinations(self, digits):
        # write your code here
        result = []
        letters_dict = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                        6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        self.dfs(digits, [], result, letters_dict)
        return result

    def dfs(self, digits, collect, result, letters_dict):
        if len(digits) < 1:
            result.append(collect[:])
            return

        letters = letters_dict[digits[0]]
        for c in letters
            collect.append(digits[i])
            self.dfs(digits, collect, result, letters_dict)
            collect.pop()




a = Solution()
print(a.letterCombinations('123'))
