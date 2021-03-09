def solution(n):
    return helper(n,{},n,0)


def helper(n, mem, last_len, step):

    if n == 0:
        if step>1:
            return 1
        else:
            return 0
    lower_bound = 1 if step < 1 else 0
    upper_bound = min(n, last_len-1)
    if (n, upper_bound) in mem:
        return mem[(n, upper_bound)]

    count = 0
    for l in range(upper_bound,lower_bound-1,-1):
        count += helper(n-l, mem, l, step+1)
    mem[(n, upper_bound)] = count
    return count


print(solution(200))