def shopping(R, B, cashiers, low, high):
    """ Using binary search for time limit T """
    if low == high:
        return low
    mid = (low + high) // 2
    # Sort cashiers by number of bits it can serve in less than mid secs
    cashiers.sort(
        key=lambda c: max(0, min(c[0], (mid - c[2]) // c[1])), reverse=True)
    # Get total of bits that top R cashiers can serve
    b = 0
    for i in range(R):
        M, S, P = cashiers[i]
        b += max(0, min(M, (mid - P) // S))
    # Check if it can serve B bits
    if b < B:
        return shopping(R, B, cashiers, mid + 1, high)
    else:
        return shopping(R, B, cashiers, low, mid)

def solve():
    T = int(input())
    for c in range(1, T + 1):
        R, B, C = map(int, input().split())
        maxS = 0
        maxP = 0
        cashiers = []
        for _ in range(C):
            M, S, P = map(int, input().split())
            maxS = max(maxS, S)
            maxP = max(maxP, P)
            cashiers.append((M, S, P))
        # Worst time to shop B bits
        maxT = maxS * B + maxP
        # Binary search for min time to shop B bits
        minT = shopping(R, B, cashiers, 1, maxT)
        print('Case #{0}: {1}'.format(c, minT))

solve()