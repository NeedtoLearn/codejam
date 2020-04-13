MAX_ROWS = 30

def getMSB(N):
    i = MAX_ROWS
    while i >= 0:
        if N & (1 << i):
            return i + 1
        i -= 1
    return 0

def solve(N):
    if N < 30:
        return [(r, 1) for r in range(1, N + 1)]
    steps = []
    on_left, over_walk = True, 0
    total_rows = getMSB(N - MAX_ROWS) # To reach N-30
    for r in range(1, total_rows + 1):
        if (N - MAX_ROWS) & (1 << (r - 1)):
            # Walk through the whole row
            row = [(r, k) for k in range(1, r + 1)]
            steps.extend(row if on_left else reversed(row))
            # Change side
            on_left = not on_left
        else:
            # Overwalk on the 1s edge one down
            over_walk += 1
            steps.append((r, 1) if on_left else (r, r))
    for i in range(1, 30 - over_walk + 1):
        steps.append((total_rows + i, 1 if on_left else total_rows + i))
    return steps

def verify(N, steps):
    import math
    S = 0
    for r, k in steps:
        S += math.factorial(r-1) // (math.factorial(k-1) * math.factorial(r - k))
    assert N == S

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    steps = solve(N)
    print('Case #{0}:'.format(t))
    for r, k in steps:
        print('%d %d' % (r, k))
    # verify(N, steps)
