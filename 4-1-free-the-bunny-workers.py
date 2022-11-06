from itertools import permutations, combinations


def solution(num_buns, num_required):
    if num_buns < 1 or num_buns > 9:
        return []
    if num_required < 0 or num_required > 9:
        return []

    # Finding out possible combinations of num_buns taken (num_buns - num_required + 1)
    # at a time, since num_required is the number of bunnies we are trying to achieve.
    # According to the problem statement, only num_required bunnies should be able to
    # open the locks and not num_required - 1; this means that num_buns - (num_required - 1)
    # have a key which (num_required - 1) bunnies do not. This way we can get the number
    # of copies of a key x.
    # These combinations would be the possible groups of bunnies which get a key x
    possibleCombinations = list(combinations(
        range(num_buns), num_buns - num_required + 1))

    result = [[] for bunny in range(num_buns)]

    for index in range(len(possibleCombinations)):
        combination = possibleCombinations[index]
        for bunny in combination:
            result[bunny].append(index)

    return result


testCase1 = {"num_buns": 2, "num_required": 1}
testCase2 = {"num_buns": 4, "num_required": 4}
testCase3 = {"num_buns": 5, "num_required": 3}


print(solution(testCase1["num_buns"], testCase1["num_required"]))
print(solution(testCase2["num_buns"], testCase2["num_required"]))
print(solution(testCase3["num_buns"], testCase3["num_required"]))
