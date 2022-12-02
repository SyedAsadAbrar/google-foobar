from itertools import permutations, combinations
import collections


def solution(w, h, s):
    # Your code here
    # print("Permutations")
    # for i in list(permutations(s * w, w * h)):
    #     print("permutation", i)

    print("s", s)

    print("Combinations")

    result_pairs = set()

    set_of_combinations = (set(combinations(s * w * h, w * h)))

    # list_of_set_of_combinations = list(set_of_combinations)

    print("------")
    for i in set_of_combinations:
        print(i)
        result_pairs.add(i)

    print("------")
    # for i in list(result_pairs):
    #     print(i)
    # print("------")


solution(2, 2, [0, 1])
# solution(2, 3, [0, 1, 2, 3])
