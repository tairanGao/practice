import copy
import math

global direction


def solution(g):
    # Your code here
    s = Sol(g)
    return s.solve()


class Sol:
    def __init__(self, g):
        self.direction = {0: [0, 0], 1: [1, 0], 2: [0, 1], 3: [1, 1]}
        self.g = g

    def solve(self):
        point_total = 0
        non_point_total = 0
        points = {}
        non_points = {}
        result = set()

        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                if self.g[i][j]:
                    point_total += 1
                    points[point_total] = [i, j]
                else:
                    non_point_total += 1
                    non_points[non_point_total] = [i,j]

        serial_num = 10 ** point_total
        pre = [[None for x in range(len(self.g[0])+1)] for y in range(len(self.g)+1)]
        sol_dict = {serial_num: pre}
        self.helper(serial_num, 1, points, non_points, sol_dict, result)
        print(result)
        print(len(result))
        return len(result)


    def final_check(self,non_points,m):
        non_point_ind = 0
        while non_point_ind < len(non_points):
            count = 0
            non_point_ind += 1
            x,y = non_points[non_point_ind]
            for d in [0,1,2,3]:
                if m[x+self.direction[d][0]][y+self.direction[d][1]]:
                    count += 1
            if count == 1:
                return False
        return True



    def helper(self, serial, curr_level, points,non_points, sol_dict, result):
        # pass
        if serial == 132000:
            print("asdasd")
        if curr_level == len(points)+1:
            temp = sol_dict[serial]
            check = self.final_check(non_points,temp)
            if check:
                result.add(get_turple(temp))
            return

        pre_level_matrix = sol_dict[serial]
        x, y = points[curr_level]
        posible_locations, violate = validate((x, y), pre_level_matrix)  # return [ori,down,right,right_down]
        if violate:
            sol_dict[serial] = False
            return

        for location in [0, 1, 2, 3]:
            curr_level_matrix = self.mark((x,y),posible_locations,pre_level_matrix,location)
            if curr_level_matrix is None:
                continue
            curr_serial = get_current_level_serial(serial, curr_level, location+1)
            sol_dict[curr_serial] = curr_level_matrix
            self.helper(curr_serial, curr_level+1, points, non_points, sol_dict, result)
        return

    def mark(self, ori, validated_location, m, marking):
        if validated_location[marking] == 0:
            return None
        curr_m = copy.deepcopy(m)
        if validated_location[marking] == 1:
            for i in range(4):
                if i == marking:
                    continue
                x = ori[0] + self.direction[i][0]
                y = ori[1] + self.direction[i][0]
                curr_m[x][y] = False
            return curr_m
        if validated_location[marking] == 2:
            for i in range(4):
                x = ori[0] + self.direction[i][0]
                y = ori[1] + self.direction[i][1]
                if i == marking:
                    curr_m[x][y] = True
                else:
                    curr_m[x][y] = False
            return curr_m



def validate(ori, m):
    # return [ori,down,right,right_down]
    # return 1: must be 1
    # return 0: must be 0
    # return 2: could be 1 or 0

    x, y = ori
    true_location = 0

    output = []

    locations = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
    for i in range(len(locations)):
        zero_count = 0
        a, b = locations[i]
        if m[a][b]:
            if true_location != 0:
                return [], True
            else:
                true_location = i
                output.append(1)

        if true_location != 0:
            output.append(0)

        elif m[a][b] is None:
            output.append(2)
        else:
            output.append(0)
            zero_count += 1
        if zero_count == 4:
            retirm [], True

    return output, False


def get_turple(m):
    return tuple(map(tuple, m))


def get_upper_level_serial(serial, current_level):
    temp = 10 ** (int(math.log(serial, 10)) - current_level + 1)
    return serial // temp * temp


def get_current_level_serial(previous_serial, current_level, location):
    #  0 : ori, 1: down, 2: right, 3: right_down
    return previous_serial + location * 10 ** (int(math.log(previous_serial, 10)) - current_level)

solution([[True, False, True], [False, True, False], [True, False, True]])
