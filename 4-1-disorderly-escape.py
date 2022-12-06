from itertools import permutations, combinations
import numpy as np


def solution(w, h, s):
    # Your code here
    # print("Permutations")
    # for i in list(permutations(s * w, w * h)):
    #     print("permutation", i)

    result_pairs = set()

    set_of_combinations = (set(combinations(list(range(s)) * w * h, w * h)))

    # list_of_set_of_combinations = list(set_of_combinations)

    for i in set_of_combinations:
        result_pairs.add(i)

    result_pairs = [np.array(list(i)).reshape((w, h))
                    for i in list(result_pairs)]

    formatted_pairs = []

    if w != h:
        if w < h:
            for i in result_pairs:
                zeros = np.zeros(h)
                formatted_pairs.append(np.insert(i, i.shape[0], zeros, axis=0))
        else:
            for i in result_pairs:
                zeros = np.zeros((w, 1))
                formatted_pairs.append(np.column_stack((i, zeros)))

    if w == h:
        formatted_pairs = result_pairs

    eigen_values = {tuple(sorted((np.linalg.eigvals(i)))): i for i in formatted_pairs}

    return len(eigen_values)


print(solution(2, 2, 2))
print(solution(2, 3, 4))
# solution(2, 3, [0, 1, 2, 3])
