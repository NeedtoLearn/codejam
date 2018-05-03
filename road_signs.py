def is_valid(signs):
    # Fix M of first sign
    M = signs[0][0] + signs[0][1]
    other_signs = list(filter(lambda sign: sign[0] + sign[1] != M, signs))
    if not other_signs:
        return True
    N = other_signs[0][0] - other_signs[0][2]
    other_signs = list(filter(lambda sign: sign[0] - sign[2] != N, other_signs))
    if not other_signs:
        return True
    # Fix N of first sign
    N = signs[0][0] - signs[0][2]
    other_signs = list(filter(lambda sign: sign[0] - sign[2] != N, signs))
    if not other_signs:
        return True
    M = other_signs[0][0] + other_signs[0][1]
    other_signs = list(filter(lambda sign: sign[0] + sign[1] != M, other_signs))
    if not other_signs:
        return True
    return False

def find_valid_sets(S, signs):
    """ Time Complexity: O(S^3) """
    for s in reversed(range(1, S + 1)):
        valid_sets = 0
        for i in range(S - s + 1):
            if is_valid(signs[i:i+s]):
                valid_sets += 1
        if valid_sets > 0:
            return s, valid_sets
    return -1, -1

def solve():
    T = int(input())
    for c in range(1, T + 1):
        S = int(input())
        signs = []
        for _ in range(S):
            D, A, B = map(int, input().split())
            signs.append((D, A, B))
        result = find_valid_sets(S, signs)
        print('Case #{0}: {1} {2}'.format(c, result[0], result[1]))

solve()