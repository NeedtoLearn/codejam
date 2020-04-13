def prepare_maze(N, path):
    M = [[0] * N for _ in range(N)]
    M[0][0] = 1
    r, c = 0, 0
    for d in path:
        if d == 'E':
            c += 1
        else:
            r += 1
        M[r][c] = 1
    return M

def find_path(N, M):
    dp = [[-1] * N for _ in range(N)]
    dp[0][0] = ''
    for r in range(N):
        for c in range(N):
            if c > 0 and dp[r][c-1] != -1 and (M[r][c] != 1 or M[r][c-1] != 1):
                dp[r][c] = dp[r][c-1] + 'E'
            if r > 0 and dp[r-1][c] != -1 and (M[r][c] != 1 or M[r-1][c] != 1):
                dp[r][c] = dp[r-1][c] + 'S'
    print(dp)
    return dp[N-1][N-1]

def solve():
    T = int(input())
    for c in range(1, T + 1):
        N = int(input())
        lydia_path = input()
        M = prepare_maze(N, lydia_path)
        print(M)
        ans = find_path(N, M)
        print('Case #{0}: {1}'.format(c, ans))

solve()
