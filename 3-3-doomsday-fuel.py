from fractions import Fraction


def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a


def inverse(a):
    tmp = [[] for _ in a]
    for i, row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret


def multiply(x, y):
    result = [[sum(Fraction(a*b).limit_denominator() for a, b in zip(X_row, Y_col))
               for Y_col in zip(*y)] for X_row in x]
    return result


def lcm(arr):
    n = len(arr)

    print(arr)

    max_num = 0
    for i in range(n):
        if (max_num < arr[i]):
            max_num = arr[i]

    res = 1

    x = 2
    while (x <= max_num):
        indexes = []
        for j in range(n):
            if (arr[j] % x == 0):
                indexes.append(j)

        if (len(indexes) >= 2):
            for j in range(len(indexes)):
                arr[indexes[j]] = int(arr[indexes[j]] / x)

            res = res * x
        else:
            x += 1

    for i in range(n):
        res = res * arr[i]

    return res


def solution(m):
    # Your code here
    matrix = [[(Fraction(num, sum(arr)) if (sum(
        arr) != 0 and num != 0) else num) for num in arr] for arr in m]

    count = 0

    for index in range(len(matrix)):
        arr = matrix[index]
        isZero = True
        for num in arr:
            if num != 0:
                isZero = False
                break
        if isZero:
            if index == 0:
                result = [1] + [num for num in arr[1:]]
                result.append(1)
                return result
            count += 1

    q = []
    r = []
    i = []

    n = []

    # make q and r matrix
    for outerIndex in range(0, len(matrix) - count):
        q.append([])
        r.append([])
        arr = matrix[outerIndex]
        for innerIndex in range(0, len(matrix) - count):
            q[outerIndex].append(arr[innerIndex])
        for innerIndex in range(len(matrix) - count, len(matrix)):
            r[outerIndex].append(arr[innerIndex])

    # make identity matrix
    for outerIndex in range(count):
        i.append([])
        for innerIndex in range(count):
            if innerIndex == outerIndex:
                i[outerIndex].append(1)
            else:
                i[outerIndex].append(0)

    for outerIndex in range(len(q)):
        n.append([])
        for innerIndex in range(len(q[outerIndex])):
            difference = i[outerIndex][innerIndex] - q[outerIndex][innerIndex]
            n[outerIndex].append(difference)

    n = inverse(n)

    for outerIndex in range(len(n)):
        for innerIndex in range(len(n[outerIndex])):
            n[outerIndex][innerIndex] = n[outerIndex][innerIndex]

    result = multiply(n, r)

    print(result)

    denominator = lcm(
        [fraction.denominator for fraction in result[0]])

    print(denominator)
    print("result", result[0])

    numerators = [int(fraction.numerator *
                  (denominator / fraction.denominator)) for fraction in result[0]]

    numerators.append(denominator)

    return numerators


testCase = [[0, 0, 0, 0, 0]]

arr = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

arr2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print(solution(testCase))
