def solve(R, B):
    num_jugglers = 0
    for i in range(1, 501):
        for j in range(i + 1):
            if B >= j:
                num_jugglers += 1
                B -= j
                R -= i - j
        if R <= i:
            return num_jugglers

T = int(input())
for c in range(1, T + 1):
    R, B = map(int, input().split())
    num_jugglers = solve(max(R, B), min(R, B))
    print('Case #{0}: {1}'.format(c, num_jugglers))