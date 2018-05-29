import sys

def solve(N):
    sold = [False] * N
    stats = [0] * N
    for _ in range(N):
        inputs = list(map(int, input().split()))
        D = inputs[0]
        flavors = inputs[1:]
        for flavor in flavors:
            stats[flavor] += 1
        if D == -1:
            exit()
        elif D == 0:
            print(-1)
            sys.stdout.flush()
        else:
            available_flavors = [flavor for flavor in flavors if not sold[flavor]]
            if not available_flavors:
                print(-1)
                sys.stdout.flush()
            else:
                available_flavors.sort(key=lambda flavor: stats[flavor])
                sold[available_flavors[0]] = True
                print(available_flavors[0])
                sys.stdout.flush()

T= int(input())
for _ in range(T):
    N = int(input())
    solve(N)