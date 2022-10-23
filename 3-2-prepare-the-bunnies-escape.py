infinity = float('inf')


def printMatrix(arr):
    for i in arr:
        print(i)
    print("")


def findMin(position, matrix, isFirstIteration=False):
    minU = minL = minR = minD = infinity

    row, col = position

    cols = len(matrix)
    rows = len(matrix[0])

    if row - 1 >= 0:
        num = matrix[col][row - 1]
        minL = num if num != 'x' else infinity

    if col - 1 >= 0:
        num = matrix[col - 1][row]
        minU = num if num != 'x' else infinity

    if not isFirstIteration:
        if row + 1 < rows:
            num = matrix[col][row + 1]
            minR = num if num != 'x' else infinity

        if col + 1 < cols:
            num = matrix[col + 1][row]
            minD = num if num != 'x' else infinity

    return min(minU, minL, minR, minD)


def findCount(position, matrix):
    row, col = position

    cols = len(matrix)
    rows = len(matrix[0])

    count = 0

    if row - 1 >= 0:
        val = matrix[col][row - 1]
        count = count + 1 if val == 1 else count

    if col - 1 >= 0:
        val = matrix[col - 1][row]
        count = count + 1 if val == 1 else count

    if row + 1 < rows:
        val = matrix[col][row + 1]
        count = count + 1 if val == 1 else count

    if col + 1 < cols:
        val = matrix[col + 1][row]
        count = count + 1 if val == 1 else count

    return count


def performOperationOnMatrix(matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    # for col in range(cols):
    #     for row in range(rows):
    #         isAWall = matrix[col][row] == 1

    #         count = findCount((row, col), matrix)

    #         canBeReplaced = count <= 1 and isAWall

    #         if canBeReplaced:
    #             matrix[col][row] = 0

    return matrix


def solution(map):
    # Your code here
    printMatrix(map)

    matrix = [['x' if num == 1 else num for num in arr] for arr in map]

    lengths = [[infinity for num in arr] for arr in map]
    lengths[0][0] = 0
    visited = [[False for num in arr] for arr in map]

    cols = len(matrix)
    rows = len(matrix[0])

    for col in range(cols):
        for row in range(rows):
            visited[col][row] = True
            if col == 0 and row == 0:
                continue
            if matrix[col][row] != 'x':
                minVal = findMin((row, col), lengths)
                lengths[col][row] = minVal + 1

    printMatrix(matrix)
    printMatrix(lengths)
    printMatrix(visited)


arr = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

arr2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

solution(arr)
