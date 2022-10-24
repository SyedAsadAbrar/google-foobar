infinity = float('inf')


# def printMatrix(arr):
#     for i in arr:
#         print(i)
#     print("")


def findNavigableNeighbours(position, matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    col, row = position

    navigableNeighbours = []

    if col - 1 >= 0 and matrix[col - 1][row] != 1:
        navigableNeighbours.append((col - 1, row))

    if row - 1 >= 0 and matrix[col][row - 1] != 1:
        navigableNeighbours.append((col, row - 1))

    if col + 1 < cols and matrix[col + 1][row] != 1:
        navigableNeighbours.append((col + 1, row))

    if row + 1 < rows and matrix[col][row + 1] != 1:
        navigableNeighbours.append((col, row + 1))

    return navigableNeighbours


def findNeighbouringWallsCount(position, matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    col, row = position

    count = 0

    if col - 1 >= 0 and matrix[col - 1][row] == 1:
        count += 1

    if row - 1 >= 0 and matrix[col][row - 1] == 1:
        count += 1

    if col + 1 < cols and matrix[col + 1][row] == 1:
        count += 1

    if row + 1 < rows and matrix[col][row + 1] == 1:
        count += 1

    return count


def findLeastNumberOfMoves(matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    lengths = [[infinity for _ in arr] for _ in matrix]
    lengths[0][0] = 0
    visited = [[False for _ in arr] for _ in matrix]

    temp = [(0, 0)]

    while len(temp) != 0:
        col, row = temp[0]
        if not visited[col][row] and matrix[col][row] != 1:
            visited[col][row] = True
            navigableNeigbours = findNavigableNeighbours((col, row), matrix)
            for neighbour in navigableNeigbours:
                neighbourCol, neighbourRow = neighbour
                lengths[neighbourCol][neighbourRow] = lengths[col][row] + 1 if lengths[col][row] + \
                    1 < lengths[neighbourCol][neighbourRow] else lengths[neighbourCol][neighbourRow]
            temp.extend(navigableNeigbours)
        temp.pop(0)

    return lengths[cols - 1][rows - 1] + 1


def solution(matrix):
    # Your code here
    cols = len(matrix)
    rows = len(matrix[0])

    if cols >= 2 and cols <= 20 and rows >= 2 and cols <= 20:
        result = []

        possibleWallRemovingPositions = []

        newMatrices = []

        # printMatrix(matrix)

        result.append(findLeastNumberOfMoves(matrix))

        for col in range(cols):
            for row in range(rows):
                if matrix[col][row] == 1:
                    value = findNeighbouringWallsCount((col, row), matrix)
                    if value == 1:
                        possibleWallRemovingPositions.append((col, row))

        # printMatrix(possibleWallRemovingPositions)

        for position in possibleWallRemovingPositions:
            col, row = position
            newMatrix = [[num for num in arr] for arr in matrix]
            newMatrix[col][row] = 0
            newMatrices.append(newMatrix)

        for matrix in newMatrices:
            result.append(findLeastNumberOfMoves(matrix))

        return min(result)


arr = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print(solution(arr))
