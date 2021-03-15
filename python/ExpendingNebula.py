from collections import deque
import copy
from cheat import *

def solution(g):
    sol = ExpendingNebua(g)
    return sol.solve()

class ExpendingNebua:
    def __init__(self, g):
        self.direction_order = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.curr_matrix = g
        self.true_list = [1, 2, 4, 8]
        self.false_list = [0, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]
        self.visited_restrictions = {}
        self.visited_bit_restrictions = {}

    def potential_with_cell_restrictions(self, left, top, value_restrict):
        if (left, top, value_restrict) in self.visited_restrictions:
            return self.visited_restrictions[(left, top, value_restrict)]

        restrictions = [None, None, None, None]

        if top is not None and left is not None:
            bin_left = bin(left)[2:].zfill(4)
            bin_top = bin(top)[2:].zfill(4)
            if bin_top[2] != bin_left[1]:
                self.visited_restrictions[(left, top, value_restrict)] = []
                return []
            else:
                restrictions = [bin_left[1], bin_top[3], bin_left[3], None]

        elif left is not None:
            bin_left = bin(left)[2:].zfill(4)
            restrictions[0] = bin_left[1]
            restrictions[2] = bin_left[3]
        elif top is not None:
            bin_top = bin(top)[2:].zfill(4)
            restrictions[0] = bin_top[2]
            restrictions[1] = bin_top[3]

        decimal_output = self.potential_with_restrictions(restrictions, value_restrict)
        self.visited_restrictions[(left, top, value_restrict)] = decimal_output
        return decimal_output

    def get_value(self,m):
        col = len(self.curr_matrix[0])
        if isinstance(m[-1], int):
            if len(m) == col:
                return m[0], None
            return None, m[-1]
        else:
            temp = len(m[-1])
            left = m[-1][-1]
            if temp == col:
                return m[-1][0], None
            else:
                top = m[-2][temp]
            return top, left

    def potential_with_restrictions(self, bit_restrict, value_restrict):
        if (tuple(bit_restrict),value_restrict) in self.visited_bit_restrictions:
            return self.visited_bit_restrictions[(tuple(bit_restrict),value_restrict)]

        decimal_output = []
        queue = deque(['0b'])

        if not bit_restrict:
            bit_restrict = [None, None, None, None]

        while queue:
            node = queue.pop()
            if len(node) == 6:
                decimal_value = int(node, 2)

                if value_restrict and decimal_value in self.true_list:
                    decimal_output.append(decimal_value)
                elif not value_restrict and decimal_value in self.false_list:
                    decimal_output.append(decimal_value)

                continue
            ind = len(node) - 2
            if bit_restrict[ind] is not None:
                node += str(bit_restrict[ind])
                queue.append(node)

            else:
                queue.append(node + '0')
                queue.append(node + '1')

        self.visited_bit_restrictions[(tuple(bit_restrict),value_restrict)] = decimal_output
        return decimal_output

    def solve(self):
        row = len(self.curr_matrix)
        col = len(self.curr_matrix[0])
        count = 0
        queue = deque([])

        if self.curr_matrix[0][0]:
            for i in self.true_list:
                queue.append([i])
        else:
            for i in self.false_list:
                queue.append([i])

        while queue:
            node = queue.pop()
            if isinstance(node[-1], list):
                if len(node) == row and len(node[-1]) == col:
                    count += 1
                    continue

            if isinstance(node[-1], int):
                pre_x, pre_y = 0, len(node) - 1
            else:
                pre_x, pre_y = len(node) - 1, len(node[-1]) - 1

            curr_y = pre_y + 1 if pre_y < col - 1 else 0
            curr_x = pre_x + 1 if curr_y == 0 else pre_x

            top_restriction, left_restriction = self.get_value(node)
            value_restriction = self.curr_matrix[curr_x][curr_y]
            potential_list = self.potential_with_cell_restrictions(left_restriction, top_restriction, value_restriction)
            for i in potential_list:
                if curr_x == 0:
                    new_node = node + [i]
                elif curr_y == 0 and curr_x == 1:
                    new_node = [node] + [[i]]
                elif curr_y == 0 and curr_x != 1:
                    new_node = node + [[i]]
                else:
                    new_node = copy.deepcopy(node)
                    new_node[-1].append(i)
                queue.append(new_node)

        return count
g = [[True, True, False, True, False, True, False, True, True, False],
     [True, True, False, False, False, False, True, True, True, False],
     [True, True, False, False, False, False, False, False, False, True],
     [False, True, False, False, False, False, True, True, False, False]
     ]

# g = [[True,True,True],[True,True,True],[True,True,True]]

print(solution(g))
print(answer(g))

