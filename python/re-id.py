def solution(pegs):
    # Your code
    if not pegs:
        return -1,-1
    l = len(pegs)
    if l % 2 == 0:
        temp = -1 * pegs[0] + pegs[-1]
        for i in range(1,l-1):
            temp += (-1) ** (i+1) * 2 * pegs[i]
        if check_valid(temp/3,pegs) < 1:
            return -1,-1
        if temp%3 == 0:
            return temp*2//3,1
        else:
            return temp*2,3
    else:
        temp = -1 * pegs[0] - pegs[-1]
        for i in range(1,l-1):
            temp += (-1) ** (i+1) * 2 * pegs[i]
        if check_valid(temp,pegs) < 1:
            return -1,-1
        return temp*2,1

def check_valid(x,pegs):
    l_list = [0]* len(pegs)
    l_list[0] = 2*x
    l_list[-1] = x
    if x < 1:
        return False
    for i in range(1,len(pegs)-1):
        l_list[i] = pegs[i] - pegs[i-1] - l_list[i-1]
        if l_list[i] < 1:
            return False
    return True


print(solution([4,17,33,51]))
