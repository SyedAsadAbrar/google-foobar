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
