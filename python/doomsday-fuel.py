from fractions import Fraction
import numpy as np


def solution(m):

    absorbing = set()
    row_total = []
    for i in range(len(m)):
        curr_total = 0
        if not any(m[i]):
            absorbing.add(i)
        else:
            for j in range(len(m[i])):
                curr_total += m[i][j]
        row_total.append(curr_total)

    R = []
    Q = []
    for i in range(len(m)):
        curr_r = []
        curr_q = []
        if i not in absorbing:
            for j in range(len(m[i])):
                if j in absorbing:
                    curr_r.append(Fraction(m[i][j], row_total[i]))
                else:
                    curr_q.append(Fraction(m[i][j], row_total[i]))
            R.append(curr_r)
            Q.append(curr_q)

    I = getIdenitityMatrix(len(Q))
    F = getMatrixInverse(matrixMinues(I, Q))
    FR = matrixDotMultiply(F, R)
    if not FR:
        return [1,1]
    analytic_solution = FR[0]
    numerators = []
    factor = 1
    for f in analytic_solution:
        factor *= f.denominator
    for i in range(len(analytic_solution)):
        analytic_solution[i] *= factor
        numerators.append(analytic_solution[i].numerator)
    result = []
    fgcd = np.gcd.reduce(numerators)


    factor = factor // fgcd
    for i in range(len(analytic_solution)):
        analytic_solution[i] /= fgcd
        result.append(int(analytic_solution[i].numerator))

    result.append(factor)
    return result


def matrixMinues(m1, m2):
    new_m = []
    for i in range(len(m1)):
        current_row = []
        for j in range(len(m2)):
            current_row.append(m1[i][j] - m2[i][j])
        new_m.append(current_row)
    return new_m


def getIdenitityMatrix(l):
    I = []
    for i in range(l):
        curr_row = []
        for j in range(l):
            if i == j:
                curr_row.append(1)
            else:
                curr_row.append(0)
        I.append(curr_row)
    return I


def transposeMatrix(m):
    return map(list, zip(*m))


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def matrixDotMultiply(m1, m2):
    result = []
    for r in m1:
        curr_row = []
        for i in range(len(m2[0])):
            total = 0
            for j in range(len(r)):
                total += r[j] * m2[j][i]
            curr_row.append(total)
        result.append(curr_row)
    return result


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


test =[
        [0]
    ]



print(solution(test))

