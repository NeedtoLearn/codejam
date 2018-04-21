from math import sqrt

def find_largest_extraP(cookies, N, P):
    """ Modified 0/1 Knapsack with weight and value are both P """
    # Create memoize array to store range of p for first ith cookies
    m = [(0, 0) for i in range(N + 1)]
    for i in range(1, N+1):
        W, H = cookies[i-1]
        # Check if lower bound of ith cookie exceed P,
        # it means we do not need to cut any more cookie.
        if 2 * W > P:
            m[i] = m[i-1]
        else:
            # Compute p range for ith cookie
            p_range = (2 * W, 2 * sqrt(W*W + H*H))
            # Scan through processed i-1 cookies in reverse order,
            # to see if we should cut this cookie.
            for j in reversed(range(i)):
                # Make sure its lower bound not exceed P,
                # it means we do not need to cut any more cookie.
                if m[j][0] + p_range[0] <= P:
                    # We can't improve the upper bound of p, so DON'T cut it
                    if m[j][1] + p_range[1] <= m[i-1][1]:
                        m[i] = m[i-1]
                    # Otherwise, cut it
                    else:
                        m[i] = (m[j][0] + p_range[0], m[j][1] + p_range[1])
                    break
    return min(m[N][1], P)

def solve():
    T = int(input())
    for c in range(1, T + 1):
        N, P = map(int, input().split())
        cookies = []
        initialP = 0
        for _ in range(N):
            W, H = map(int, input().split())
            cookies.append((min(W, H), max(W, H)))
            initialP += 2 * (W + H)
        extraP = find_largest_extraP(cookies, N, P - initialP)
        print('Case #{0}: {1}'.format(c, initialP + extraP))

solve()