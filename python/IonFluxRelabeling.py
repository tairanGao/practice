def solution(h, q):
    # Your code
    total = 0
    level_dict = {}
    for i in range(h):
        total += 2 ** i
        level_dict[i] = []

    count = 0
    level = h - 1
    result = []
    while count < total:
        count += 1
        level_dict[level].append(count)
        while len(level_dict[level]) != 0 and len(level_dict[level]) % 2 == 0:
            level -= 1
            count += 1
            level_dict[level].append(count)
        level = h - 1

    for i in q:
        if i >= total:
            result.append(-1)
            continue
        for j in range(h):
            if i in level_dict[j]:
                result.append(level_dict[j-1][level_dict[j].index(i)//2])
    print(result)

solution(3, [7, 3, 5, 1])
