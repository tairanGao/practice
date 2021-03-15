class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        return self.helper(triangle,0,0,{})

    def helper(self,triangle,i,j,visited):
        if not triangle[i]:
            return 0
        if (i,j) in visited:
            return visited[(i,j)]
        if i == len(triangle)-1:
            return triangle[i][j]

        left = self.helper(triangle, i+1, j,visited)
        right = self.helper(triangle, i+1, j+1,visited)
        result = min(right, left) + triangle[i][j]
        visited[(i,j)] = result
        return result







triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

a = Solution()
print(a.minimumTotal(triangle))