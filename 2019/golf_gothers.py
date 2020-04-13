import sys

blades = ' '.join(['18'] * 18)

def solve():
    counts = []
    for _ in range(365):
        print(blades)
        sys.stdout.flush()
        res = list(map(int, input().split()))
        if len(res) != 18:
            exit()
        counts.append(sum(res))
    # Find min number of 18 so that all counts are equal
    for j in range(10):
        pass

T, N, M = map(int, input().split())
for _ in range(T):
    solve()