def find_A(N):
    A, idx = 0, 0
    while N > 0:
        if N % 10 == 4:
            A += 10 ** idx
        N //= 10
        idx += 1
    return A

def find_pair(N):
    A = find_A(N)
    return A, N - A

T = int(input())
for c in range(1, T + 1):
    N = int(input())
    A, B = find_pair(N)
    print('Case #{0}: {1} {2}'.format(c, A, B))
