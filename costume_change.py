def solve(N, A):
    change_rows = []
    for r in range(N):
        exists = set(A[r])
        indexes = [(c, A[r][c]) for c in range(N) if A[r][c] in exists]
        change_rows.append(indexes)
    change_cols = []
    for c in range(N):
        col = [A[r][c] for r in range(N)]
        exists = set(col)
        indexes = [(r, c) for r, c in enumerate(col) if c in exists]
        change_rows.append(indexes)
    for row in change_rows:
        pass

T = int(input())
for c in range(1, T+1):
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    changes = solve(N, A)
    print('Case #{0}: {1}'.format(c, changes))