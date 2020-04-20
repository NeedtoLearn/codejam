def get_coefficients(N):
    """ Express POSITIVE ODD number N as sum of (+-)2**i where i >= 0 """
    if N == 1:
        return [1]
    if ((N-1) // 2) % 2 == 0:
        return [-1] + get_coefficients((N + 1) // 2)
    return [1] + get_coefficients((N-1) // 2)

def solve(X, Y):
    if (abs(X) + abs(Y)) % 2 == 0:
        return 'IMPOSSIBLE'
    X_sign = 1 if X > 0 else -1
    Y_sign = 1 if Y > 0 else -1
    directions = ''
    for coef in get_coefficients(abs(X) + abs(Y)):
        if X % 2 != 0:
            directions += 'E' if X_sign * coef > 0 else 'W'
            X -= X_sign * coef
        else:
            directions += 'N' if Y_sign * coef > 0 else 'S'
            Y -= Y_sign * coef
        X //= 2
        Y //= 2
    return directions

T = int(input())
for t in range(1, T + 1):
    X, Y = map(int, input().split())
    ans = solve(X, Y)
    print('Case #{0}: {1}'.format(t, ans))
