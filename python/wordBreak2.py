class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        if not wordDict or s == "":
            return []
        max_len = max([len(x) for x in wordDict])
        return self.helper(s,0,wordDict, {},max_len)


    def helper(self,s,left,wordDict,visited,max_len):
        if left >= len(s):
            return []
        if left not in visited:
            visited[left] = []
        else:
            return visited[left]

        for i in range(left,len(s)):
            if i + 1 - left > max_len:
                break
            if s[left:i + 1] in wordDict:
                return_list = self.helper(s, i+1, wordDict,visited,max_len)
                if return_list:
                    for str in return_list:
                        visited[left].append(s[left:i + 1] + ' ' + str)

        if s[left:] in wordDict:
            visited[left].append(s[left:])

        return visited[left]


sol = Solution()
s = "Catmat"
k = ["Cat","mat","Ca","tm","at","C","Dog","og","Do"]

wordSet = set()
for i in k:
    wordSet.add(i)

print(sol.wordBreak(s, wordSet))
