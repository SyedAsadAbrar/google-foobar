from fractions import Fraction
import numpy as np


def printMatrix(m):
    for arr in m:
        print(arr)
    print("")


def solution(m):
    # Your code here
    matrix = [[(Fraction(num, sum(arr)) if (sum(
        arr) != 0 and num != 0) else num) for num in arr] for arr in m]

    absorbingRows = []
    nonAbsorbingRows = []

    for index in range(len(matrix)):
        arr = matrix[index]
        arrSum = sum(arr)
        if arrSum == 0:
            if index == 0:
                result = [1] + [num for num in arr[1:]] + [1]
                return result
            absorbingRows.append(index)
        else:
            nonAbsorbingRows.append(index)

    q = []
    r = []
    i = []

    n = []

    # make q and r matrix
    for outerIndex in nonAbsorbingRows:
        arr = matrix[outerIndex]
        q.append([])
        for innerIndex in nonAbsorbingRows:
            q[len(q) - 1].append(arr[innerIndex])

        r.append([])
        for innerIndex in absorbingRows:
            r[len(r) - 1].append(arr[innerIndex])

    q = np.matrix(q, dtype=float)

    r = np.matrix(r, dtype=float)

    i = np.identity(len(q))

    n = (i - q)

    n = np.linalg.inv(n)

    result = np.dot(n, r)

    result = [[Fraction(decimal).limit_denominator() for decimal in arr]
              for arr in np.asarray(result)]

    denominator = np.lcm.reduce(
        [fraction.denominator for fraction in result[0]])

    numerators = [int(fraction.numerator *
                  (denominator / fraction.denominator)) for fraction in result[0]]

    return numerators + [denominator]


test1 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


test2 = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]


test3 = [
    [1, 2, 3, 0, 0, 0],
    [4, 5, 6, 0, 0, 0],
    [7, 8, 9, 1, 0, 0],
    [0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]


test4 = [
    [0]
]


test5 = [
    [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
    [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
    [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
    [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


test6 = [
    [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
    [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
    [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
    [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
    [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


test7 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


test8 = [
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


test9 = [
    [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
    [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
    [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


test10 = [
    [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
    [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
    [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
    [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


testCases = [test1, test2, test3, test4,
             test5, test6, test7, test8, test9, test10]

results = [[7, 6, 8, 21], [0, 3, 2, 9, 14], [1, 2, 3], [1, 1], [1, 2, 3, 4, 5, 15], [
    4, 5, 5, 4, 2, 20], [1, 1, 1, 1, 1, 5], [2, 1, 1, 1, 1, 6], [6, 44, 4, 11, 22, 13, 100], [1, 1, 1, 2, 5]]

for index in range(len(testCases)):
    testCase = testCases[index]
    print(results[index] == solution(testCase))
