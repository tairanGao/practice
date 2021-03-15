import time
from cheat import *

from collections import deque
def solution(g):
    sol = ExpendingNebua(g)

    return sol.solve_2(None, 0)


class ExpendingNebua:
    def __init__(self, g):
        self.curr_matrix = g
        self.state = {}
        self.visited_restrictions = {(8, 9, False): [], (12, 5, True): [8], (15, 13, False): [9, 11], (5, 2, True): [],
                                     (13, 4, False): [], (0, 2, True): [4], (6, 13, False): [9, 11], (12, 12, True): [],
                                     (None, 9, False): [9, 10, 11], (10, 12, False): [3], (0, 15, True): [],
                                     (3, 7, False): [], (11, 5, True): [], (1, 2, False): [6], (4, 12, True): [],
                                     (0, 6, True): [4], (11, 0, True): [1], (5, None, True): [8], (14, 10, False): [],
                                     (4, 1, True): [8], (12, 7, False): [12, 14], (None, 5, False): [9, 10, 11],
                                     (15, 15, True): [], (5, 0, False): [], (10, None, False): [3, 5, 7],
                                     (11, 9, True): [], (14, None, False): [9, 11, 13, 15], (9, 9, False): [],
                                     (4, None, False): [10, 12, 14], (15, 2, True): [], (10, 10, True): [],
                                     (0, 1, False): [], (3, 9, True): [], (11, None, False): [3, 5, 7],
                                     (7, 5, False): [9, 11], (None, 10, True): [4], (15, 14, True): [],
                                     (10, 15, True): [], (3, 4, True): [1], (11, 2, False): [5, 7], (14, 8, True): [],
                                     (4, 3, False): [12, 14], (None, 3, True): [], (2, 4, False): [3],
                                     (10, 6, True): [], (8, 10, False): [6], (14, 5, True): [], (9, 15, True): [],
                                     (None, 6, True): [4], (15, 12, False): [], (13, 6, False): [],
                                     (13, 3, False): [12, 14], (6, 2, False): [], (7, 7, True): [], (9, 10, True): [4],
                                     (None, 8, False): [0, 3], (10, 13, False): [], (3, 6, False): [5, 7],
                                     (1, 1, False): [], (7, 10, True): [], (9, 3, True): [], (2, 2, True): [],
                                     (13, 15, False): [12, 14], (8, 12, True): [2], (14, 11, False): [13, 15],
                                     (12, 0, False): [], (None, 4, False): [0, 3], (2, 7, True): [],
                                     (5, 15, False): [12, 14], (1, 6, False): [6], (13, 1, True): [8],
                                     (6, 14, False): [], (6, 0, True): [], (9, None, True): [2, 4], (8, 9, True): [],
                                     (2, 14, True): [], (9, 8, False): [0], (13, 4, True): [], (3, None, True): [1],
                                     (0, 2, False): [6], (6, 13, True): [], (8, 0, True): [2], (1, 7, True): [],
                                     (7, 4, False): [], (12, 12, False): [], (8, None, False): [0, 6],
                                     (13, 13, True): [8], (11, 5, False): [], (1, 2, True): [4], (4, 12, False): [],
                                     (12, 2, True): [], (2, 5, False): [], (5, 13, True): [8], (1, 11, True): [],
                                     (8, 11, False): [], (5, None, False): [10, 12, 14], (12, 7, True): [],
                                     (15, 15, False): [13, 15], (5, 0, True): [], (13, 2, False): [],
                                     (10, None, True): [1], (0, 4, True): [2], (6, 3, False): [13, 15],
                                     (11, 9, False): [], (12, 14, True): [], (14, None, True): [], (4, None, True): [8],
                                     (10, 10, False): [5, 7], (0, 1, True): [], (3, 9, False): [], (11, 7, True): [],
                                     (1, 0, False): [0], (4, 14, True): [], (13, 14, False): [], (0, 8, True): [2],
                                     (11, 2, True): [], (14, 8, False): [], (4, 3, True): [], (12, 1, False): [10],
                                     (None, 3, False): [12, 13, 14, 15], (15, 9, True): [], (5, 14, False): [],
                                     (10, 6, False): [5, 7], (11, 11, True): [], (9, 15, False): [], (15, 12, True): [],
                                     (10, 8, True): [1], (0, 3, False): [], (3, 11, True): [], (7, 7, False): [13, 15],
                                     (12, 13, False): [10], (15, 5, True): [], (None, 8, True): [1, 2],
                                     (10, 13, True): [], (3, 6, True): [], (11, 4, False): [3], (14, 14, True): [],
                                     (4, 13, False): [10], (9, 3, False): [], (None, 1, True): [8],
                                     (2, 2, False): [5, 7], (10, 4, True): [1], (8, 12, False): [0], (14, 11, True): [],
                                     (9, 13, True): [], (None, 4, True): [1, 2], (2, None, False): [3, 5, 7],
                                     (13, 1, False): [10], (6, 0, False): [], (11, 8, False): [3],
                                     (6, None, False): [9, 11, 13, 15], (9, None, False): [0, 6], (7, 1, True): [],
                                     (15, None, False): [9, 11, 13, 15], (9, 8, True): [2], (10, 11, False): [],
                                     (3, None, False): [3, 5, 7], (3, 8, False): [3], (8, 0, False): [0],
                                     (1, 7, False): [], (7, 4, True): [], (9, 1, True): [], (8, None, True): [2, 4],
                                     (2, 0, True): [1], (13, 13, False): [10], (7, 13, True): [], (8, 14, True): [4],
                                     (14, 9, False): [9, 11], (12, 2, False): [], (None, 2, False): [5, 6, 7],
                                     (2, 5, True): [], (5, 13, False): [10], (10, 7, False): [], (6, 6, True): [],
                                     (1, 11, False): [], (8, 11, True): [], (2, 12, True): [1], (9, 14, False): [6],
                                     (13, 2, True): [], (0, 4, False): [0], (6, 3, True): [], (8, 2, True): [4],
                                     (1, 5, True): [], (7, 6, False): [], (12, 14, False): [], (13, 11, True): [],
                                     (6, 10, True): [], (11, 7, False): [], (1, 0, True): [2], (4, 14, False): [],
                                     (9, 2, False): [6], (2, 3, False): [], (5, 11, True): [], (13, 14, True): [],
                                     (0, 8, False): [0], (1, 9, True): [], (14, 2, False): [], (8, 13, False): [],
                                     (12, 1, True): [8], (15, 9, False): [9, 11], (5, 14, True): [], (13, 0, False): [],
                                     (1, None, True): [2, 4], (6, 1, False): [9, 11], (11, 11, False): [],
                                     (7, None, True): [], (12, 8, True): [], (2, 15, False): [], (5, 7, True): [],
                                     (10, 8, False): [3], (0, 3, True): [], (3, 11, False): [], (8, 1, False): [],
                                     (0, None, False): [0, 6], (4, 8, True): [], (12, 13, True): [8],
                                     (15, 5, False): [9, 11], (13, 12, False): [], (0, 10, True): [4],
                                     (11, 4, True): [1], (14, 14, False): [], (4, 13, True): [8],
                                     (12, 3, False): [12, 14], (None, 1, False): [9, 10, 11], (15, 11, True): [],
                                     (5, 12, False): [], (10, 4, False): [3], (11, 13, True): [], (1, 10, False): [6],
                                     (4, 4, True): [], (9, 13, False): [], (2, None, True): [1],
                                     (None, None, True): [1, 2, 4, 8], (0, 5, False): [], (3, 13, True): [],
                                     (11, 8, True): [1], (6, None, True): [], (7, 1, False): [9, 11],
                                     (12, 15, False): [12, 14], (15, 7, True): [], (10, 11, True): [],
                                     (3, 8, True): [1], (11, 6, False): [5, 7], (14, 12, True): [],
                                     (4, 15, False): [12, 14], (9, 1, False): [], (None, 15, True): [],
                                     (2, 0, False): [3], (10, 2, True): [], (13, 6, True): [], (3, 1, True): [],
                                     (7, 13, False): [9, 11], (8, 14, False): [6], (14, 9, True): [],
                                     (None, 2, True): [4], (15, 8, False): [], (10, 7, True): [], (6, 6, False): [],
                                     (11, 10, False): [5, 7], (14, 0, True): [], (7, 3, True): [], (2, 12, False): [3],
                                     (9, 14, True): [4], (10, 9, False): [], (3, 10, False): [5, 7], (8, 2, False): [6],
                                     (1, 5, False): [], (7, 6, True): [], (9, 7, True): [], (15, 4, False): [],
                                     (13, 11, False): [12, 14], (6, 10, False): [], (0, 9, False): [],
                                     (7, 15, True): [], (14, 15, False): [13, 15], (9, 2, True): [4],
                                     (None, 0, False): [0, 3], (2, 3, True): [], (5, 11, False): [12, 14],
                                     (10, 5, False): [], (6, 4, True): [], (1, 9, False): [], (8, 13, True): [],
                                     (2, 10, True): [], (9, 12, False): [0], (13, 0, True): [], (0, 6, False): [6],
                                     (6, 1, True): [], (8, 4, True): [2], (14, 3, False): [13, 15],
                                     (7, None, False): [9, 11, 13, 15], (7, 0, False): [], (12, 8, False): [],
                                     (2, 15, True): [], (5, 7, False): [12, 14], (13, 9, True): [8], (6, 8, True): [],
                                     (None, 0, True): [1, 2], (8, 1, True): [], (0, None, True): [2, 4],
                                     (4, 8, False): [], (9, 0, False): [0], (2, 1, False): [], (5, 9, True): [8],
                                     (13, 12, True): [], (0, 10, False): [6], (1, 15, True): [], (7, 12, False): [],
                                     (8, 15, False): [], (12, 3, True): [], (15, 11, False): [13, 15],
                                     (5, 12, True): [], (6, 7, False): [13, 15], (11, 13, False): [],
                                     (1, 10, True): [4], (4, 4, False): [], (12, 10, True): [], (2, 13, False): [],
                                     (5, 5, True): [8], (None, None, False): [0, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15],
                                     (0, 5, True): [], (3, 13, False): [], (8, 3, False): [], (1, 4, False): [0],
                                     (4, 10, True): [], (12, 15, True): [], (15, 7, False): [13, 15],
                                     (13, 10, False): [], (0, 12, True): [2], (15, 14, False): [],
                                     (6, 11, False): [13, 15], (11, 6, True): [], (14, 12, False): [],
                                     (4, 15, True): [], (None, 15, False): [12, 13, 14, 15], (5, 10, False): [],
                                     (10, 2, False): [5, 7], (0, 9, True): [], (3, 1, False): [], (11, 15, True): [],
                                     (1, 8, False): [0], (4, 6, True): [], (15, 8, True): [], (0, 7, False): [],
                                     (3, 15, True): [], (11, 10, True): [], (14, 0, False): [], (7, 3, False): [13, 15],
                                     (12, 9, False): [10], (15, 1, True): [], (5, 6, False): [], (14, 2, True): [],
                                     (10, 9, True): [], (3, 10, True): [], (4, 9, False): [10], (9, 7, False): [],
                                     (15, 4, True): [], (None, 13, True): [8], (10, 0, True): [1], (0, 11, False): [],
                                     (3, 3, True): [], (7, 15, False): [13, 15], (14, 15, True): [],
                                     (2, 14, False): [5, 7], (15, 10, False): [], (10, 5, True): [], (6, 4, False): [],
                                     (11, 12, False): [3], (14, 6, True): [], (4, 5, False): [10],
                                     (2, 10, False): [5, 7], (9, 12, True): [2], (3, 12, False): [3],
                                     (8, 4, False): [0], (14, 3, True): [], (7, 0, True): [], (9, 5, True): [],
                                     (15, 6, False): [], (13, 9, False): [10], (6, 8, False): [], (7, 9, True): [],
                                     (14, 13, False): [9, 11], (9, 0, True): [2], (None, 14, False): [5, 6, 7],
                                     (2, 1, True): [], (5, 9, False): [10], (10, 3, False): [], (3, 0, False): [3],
                                     (1, 15, False): [], (7, 12, True): [], (8, 15, True): [], (2, 8, True): [1],
                                     (6, 7, True): [], (8, 6, True): [4], (14, 1, False): [9, 11], (7, 2, False): [],
                                     (12, 10, False): [], (2, 13, True): [], (5, 5, False): [10], (13, 7, True): [],
                                     (6, 14, True): [], (8, 3, True): [], (1, 4, True): [2], (4, 10, False): [],
                                     (9, 6, False): [6], (13, 10, True): [], (0, 12, False): [0], (6, 11, True): [],
                                     (1, 13, True): [], (7, 14, False): [], (5, 10, True): [], (6, 5, False): [9, 11],
                                     (11, 15, False): [], (1, 8, True): [2], (4, 6, False): [], (12, 4, True): [],
                                     (2, 11, False): [], (5, 3, True): [], (0, 7, True): [], (3, 15, False): [],
                                     (8, 5, False): [], (12, 9, True): [8], (15, 1, False): [9, 11], (5, 6, True): [],
                                     (13, 8, False): [], (0, 14, True): [4], (6, 9, False): [9, 11], (4, 9, True): [8],
                                     (None, 13, False): [9, 10, 11], (5, 8, False): [], (10, 0, False): [3],
                                     (0, 11, True): [], (3, 3, False): [], (11, 1, True): [], (1, 14, False): [6],
                                     (4, 0, True): [], (15, 10, True): [], (11, 12, True): [1], (14, 6, False): [],
                                     (4, 5, True): [8], (12, 11, False): [12, 14], (15, 3, True): [], (5, 4, False): [],
                                     (3, 12, True): [1], (4, 11, False): [12, 14], (9, 5, False): [], (15, 6, True): [],
                                     (None, 11, True): [], (10, 14, True): [], (0, 13, False): [], (3, 5, True): [],
                                     (7, 9, False): [9, 11], (14, 13, True): [], (None, 14, True): [4],
                                     (10, 3, True): [], (3, 0, True): [1], (11, 14, False): [5, 7], (14, 4, True): [],
                                     (4, 7, False): [12, 14], (None, 7, True): [], (2, 8, False): [3],
                                     (3, 14, False): [5, 7], (8, 6, False): [6], (14, 1, True): [], (7, 2, True): [],
                                     (9, 11, True): [], (15, 0, False): [], (13, 7, False): [12, 14],
                                     (12, 6, False): [], (7, 11, True): [], (9, 6, True): [4],
                                     (None, 12, False): [0, 3], (10, 1, False): [], (3, 2, False): [5, 7],
                                     (1, 13, False): [], (7, 14, True): [], (2, 6, True): [], (6, 5, True): [],
                                     (8, 8, True): [2], (14, 7, False): [13, 15], (12, 4, False): [], (2, 11, True): [],
                                     (5, 3, False): [12, 14], (13, 5, True): [8], (6, 12, True): [],
                                     (1, None, False): [0, 6], (8, 5, True): [], (15, None, True): [],
                                     (9, 4, False): [0], (13, 8, True): [], (0, 14, False): [6], (6, 9, True): [],
                                     (1, 3, True): [], (7, 8, False): [], (5, 8, True): [], (11, 1, False): [],
                                     (1, 14, True): [4], (4, 0, False): [], (13, None, True): [8], (2, 9, False): [],
                                     (5, 1, True): [8], (8, 7, False): [], (12, 11, True): [], (15, 3, False): [13, 15],
                                     (5, 4, True): [], (12, None, False): [10, 12, 14], (0, 0, True): [2],
                                     (6, 15, False): [13, 15], (4, 11, True): [], (None, 11, False): [12, 13, 14, 15],
                                     (10, 14, False): [5, 7], (0, 13, True): [], (3, 5, False): [], (11, 3, True): [],
                                     (1, 12, False): [0], (4, 2, True): [], (11, 14, True): [], (14, 4, False): [],
                                     (4, 7, True): [], (12, 5, False): [10], (None, 7, False): [12, 13, 14, 15],
                                     (15, 13, True): [], (5, 2, False): [], (3, 14, True): [], (9, 11, False): [],
                                     (15, 0, True): [], (None, 9, True): [8], (10, 12, True): [1], (0, 15, False): [],
                                     (3, 7, True): [], (1, 6, True): [4], (7, 11, False): [13, 15],
                                     (None, 12, True): [1, 2], (10, 1, True): [], (3, 2, True): [], (11, 0, False): [3],
                                     (14, 10, True): [], (4, 1, False): [10], (None, 5, True): [8],
                                     (2, 6, False): [5, 7], (8, 8, False): [0], (14, 7, True): [], (9, 9, True): [],
                                     (15, 2, False): [], (13, 5, False): [10], (6, 12, False): [],
                                     (11, None, True): [1], (7, 5, True): [], (9, 4, True): [2],
                                     (None, 10, False): [5, 6, 7], (10, 15, False): [], (3, 4, False): [3],
                                     (1, 3, False): [], (7, 8, True): [], (2, 4, True): [1], (8, 10, True): [4],
                                     (14, 5, False): [9, 11], (13, None, False): [10, 12, 14],
                                     (None, 6, False): [5, 6, 7], (2, 9, True): [], (5, 1, False): [10],
                                     (13, 3, True): [], (6, 2, True): [], (8, 7, True): [], (9, 10, False): [6],
                                     (12, None, True): [8], (0, 0, False): [0], (6, 15, True): [], (1, 1, True): [],
                                     (7, 10, False): [], (13, 15, True): [], (11, 3, False): [], (1, 12, True): [2],
                                     (4, 2, False): [], (12, 0, True): [], (2, 7, False): [], (5, 15, True): [],
                                     (12, 6, True): []}
        self.num_row = len(self.curr_matrix)
        self.num_col = len(self.curr_matrix[0])

    def solve_2(self, left_column,column_num):

        if column_num == self.num_col:
            return 1

        hashable_lc = tuple(left_column) if left_column else None
        if (hashable_lc, column_num) in self.state:
            return self.state[(hashable_lc, column_num)]

        count = 0
        queue = deque([])
        top_value = None
        left_value = left_column[0] if left_column else None
        has_gas = self.curr_matrix[0][column_num]
        possible_values = self.visited_restrictions[(left_value, top_value, has_gas)]

        for i in possible_values:
            queue.append([i])

        while queue:
            node = queue.popleft()
            if len(node) == self.num_row:
                full_column = node
                count += self.solve_2(full_column, column_num + 1)
                continue
            next_row = len(node)

            top_value = node[-1]
            left_value = left_column[next_row] if left_column else None
            has_gas = self.curr_matrix[next_row][column_num]
            possible_values = self.visited_restrictions[(left_value, top_value, has_gas)]
            for i in possible_values:
                queue.append(node + [i])

        self.state[(hashable_lc, column_num)] = count
        return count



# g = [[True, True, False, True, False, True, False, True, True, False],
#      [True, True, False, False, False, False, True, True, True, False],
#      [True, True, False, False, False, False, False, False, False, True],
#      [False, True, False, False, False, False, True, True, False, False]
#      ]

# g = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False],
#      [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False],
#      [True, False, True, False, False, True, True, True]]
#
g = [[True, False, False, True, False, True, False, True, True, False, True, True],
     [True, True, False, False, False, False, True, True, True, False, True, True],
     [True, True, False, False, False, False, False, False, False, True, True, True],
     [False, True, False, False, False, False, True, False, False, False, True, True]
     ]
# g = [[True, False, True], [False, True, False], [True, False, True]]
time_start = time.clock()
print(solution(g))
time_elapsed = (time.clock() - time_start)
print(time_elapsed)
time_start = time.clock()
print(answer(g))
time_elapsed = (time.clock() - time_start)
print(time_elapsed)
