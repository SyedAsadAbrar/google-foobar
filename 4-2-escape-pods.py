def solution(entrances, exits, path):
    # Your code here
    maxPossible = [sum(
        path[index]) if index not in entrances and index not in exits else 0 for index in range(len(path))]

    answer = [0 for arr in path]


testCase1 = {"entrances": [0], "exits": [3], "path": [
    [0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]}
testCase2 = {"entrances": [0, 1], "exits": [4, 5], "path": [[0, 0, 4, 6, 0, 0], [
    0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]}

print(solution(testCase1["entrances"], testCase1["exits"], testCase1["path"]))
print(solution(testCase2["entrances"], testCase2["exits"], testCase2["path"]))
