def solve(mat, N):
    k = sum(mat[i][i] for i in range(N))
    r = 0
    for i in range(N):
        if len(set(mat[i])) < N:
            r += 1
    c = 0
    for i in range(N):
        if len(set(mat[j][i] for j in range(N))) < N:
            c += 1
    return k, r, c


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    mat = [
        list(map(int, input().split())) for _ in range(N)
    ]
    k, r, c = solve(mat, N)
    print('Case #{0}: {1} {2} {3}'.format(t, k, r, c))
