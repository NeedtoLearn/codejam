def getK(N):
    K = 1
    while K * (K + 1) // 2 <= N - 1:
        K += 1
    return K - 1

def solve(N):
    K = getK(N)
    steps = [(1, 1)]
    for i in range(1, K + 1):
        steps.append((i + 1, 2))
    # Find remaining steps
    remain = N - 1 - K * (K + 1) // 2
    for i in range(remain):
        steps.append((K + 1 + i, 1))
    return steps

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    steps = solve(N)
    print('Case #{0}:'.format(t))
    for r, k in steps:
        print('%d %d' % (r, k))
