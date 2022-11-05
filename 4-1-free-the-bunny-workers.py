from itertools import permutations, combinations


def solution(num_buns, num_required):
    if num_buns < 1 or num_buns > 9:
        return []
    if num_required < 0 or num_required > 9:
        return []

    perm = permutations(range(num_buns), num_required)
    comb = combinations(range(num_buns), num_required)

    print("Permutations")
    for i in list(perm):
        print(i)
    print("Combinations")
    for i in list(comb):
        print(i)
    print(num_buns, num_required)


testCase1 = {"num_buns": 2, "num_required": 1}
testCase2 = {"num_buns": 4, "num_required": 4}
testCase3 = {"num_buns": 5, "num_required": 3}


solution(testCase1["num_buns"], testCase1["num_required"])
solution(testCase2["num_buns"], testCase2["num_required"])
solution(testCase3["num_buns"], testCase3["num_required"])
