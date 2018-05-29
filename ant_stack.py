def stack_ants_recursive(N, ants, cur_len, cur_weight):
    if N == 0:
        return cur_len
    # Check if next ant can climb up to cur_stack
    if cur_weight > 6 * ants[0]:
        return stack_ants_recursive(
            N-1, ants[1:], cur_len, cur_weight)
    return max(
        stack_ants_recursive(N-1, ants[1:], cur_len, cur_weight),
        stack_ants_recursive(N-1, ants[1:], cur_len + 1, cur_weight + ants[0]))

def stack_ants_dp(N, W, ants):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        for w in range(1, W + 1):
            if w < ants[n - 1]:
                dp[n][w] = dp[n-1][w]
            else:
                dp[n][w] = max(
                    dp[n-1][w],
                    dp[n-1][min(6 * ants[n-1], w - ants[n-1])] + 1)
    return dp[N][W]

def solve():
    T = int(input())
    for c in range(1, T + 1):
        N = int(input())
        ants = list(map(int, input().split()))
        # size = stack_ants_recursive(N, ants, 0, 0)
        size = stack_ants_dp(N, 7000, ants)
        print('Case #{0}: {1}'.format(c, size))

solve()
