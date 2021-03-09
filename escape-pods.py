from collections import deque

def solution(entrances, exits, path):
    # Your code here
    n = len(path) # number of rows
    m = len(path[0]) # number of column
    load = [[0 for i in range(m)] for j in range(n)]
    result = 0

    while True:
        if result >= 2000000:
            return 2000000
        add_on = dfs(entrances, exits, path, load)
        if add_on <= 0:
            break
        result += add_on
    return result


def dfs(entrances,exits,path,load):
    queue = deque([])
    coming_node = {}


    for node in entrances:
        queue.append((node,2000000))
        coming_node[node] = -1  # source
    check = False
    max_flow = 0
    while queue:
        (row,max_flow) = queue.pop()
        if row in exits:
            check = True # found exit
            break
        for i in range(len(path[row])):
            if path[row][i] - load[row][i] == 0:
                continue
            if i in coming_node:
                continue
            coming_node[i] = row
            max_flow = min(max_flow,path[row][i] - load[row][i])
            queue.append((i, max_flow))

    if check:
        current_node = row
        previous_node = coming_node[row]
        while previous_node != -1:
            load[previous_node][current_node] += max_flow
            current_node = previous_node
            previous_node = coming_node[current_node]
    else:
        max_flow = 0

    return max_flow



print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
