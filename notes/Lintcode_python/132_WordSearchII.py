class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []
        result = []
        check = False
        for w in words:
            if not w:
                continue
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == w[0]:
                        if self.dfs(board, set(), w[1:], (i,j)):
                            result.append(w)
                            check = True
                            break
                if check:
                    break
            if check:
                check = False
                continue

        return result

    def dfs(self, board, visited, word, curr_pos):

        if not word:
            return True

        x, y = curr_pos
        visited.add(curr_pos)

        for d in [(0,1),(1,0),(-1,0),(0,-1)]:
            if 0<= x+d[0] < len(board) and 0<=y+d[1] <len(board[0]):
                if (x+d[0], y+d[1]) in visited:
                    continue
                if board[x+d[0]][y+d[1]] == word[0]:
                    if self.dfs(board, visited.copy(), word[1:], (x+d[0], y+d[1])):
                        return True

        return False



sol = Solution()

board = ["babcbababcacab","cacccbaaabccbb","accbaabbbccacc","acbaabcabcbbab","caacaaabbcaaca","bbacbcccbcacbc","acaccacabacaca","bcacbbcabbaaaa","cccaacbcbaacba","acaccacaccbabb","bacacbbccaabcb","aaccacbacabcca","abcbcbbbabcaba","bbcacbcaaababa","acaabccabbcaab"]
words = ["accbbcba","ccbaaabccb","ccbaaabccbz","babcbababcacabbbccbaaabcccacaccbaabbbccacc","babcbababcacabbbccbaaabcccacaccbaabbbccaccz","babcbababcacabbbccbaaabcccacaccbaabbbccacce","babcbababcacabbbccbaaabcccacaccbaabbbccacczz","babcbababcacabbbccbaaabcccacaccbaabbbccaccp","babcbababcacabbbccbaaabcccacaccbaabbbccaccw","babcbababcacabbbccbaaabcccacaccbaabbbccaccl","babcbababcacabbbccbaaabcccacaccbaabbbccaccm","babcbababcacabbbccbaaabcccacaccbaabbbccaccn","babcbababcacabbbccbaaabcccacaccbaabbbccaccv","babcbababcacabbbccbaaabcccacaccbaabbbccaccx","babcbababcacabbbccbaaabcccacaccbaabbbccaccy"]


print(sol.wordSearchII(board, words))