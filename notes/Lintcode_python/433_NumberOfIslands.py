from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        visited = set()
        output = 0
        island_deque = deque()

        for i in range(row):
            for j in range(col):
                if (i, j) not in visited and grid[i][j] == 1:
                    output += 1
                    island_deque.append((i, j))
                    while island_deque:
                        location = island_deque.popleft()
                        x, y = location
                        if location not in visited and grid[x][y] == 1:
                            if x + 1 < row:
                                island_deque.append((x + 1, y))
                            if x - 1 >= 0:
                                island_deque.append((x - 1, y))
                            if y + 1 < col:
                                island_deque.append((x, y + 1))
                            if y - 1 >= 0:
                                island_deque.append((x, y - 1))
                        visited.add(location)

        return output

Input = \
    [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]

sol = Solution()
print(sol.numIslands(Input))