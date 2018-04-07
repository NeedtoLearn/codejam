import sys

def solve(A):
    for r in range(2, 4):
        for c in range(2, A // 4):
            print(r, c)
            sys.stdout.flush()
            x, y = map(int, input().split())
            if x == 0 and y == 0:
                return
            if x == -1 and y == -1:
                exit()
    solve(A)

T = int(input())
for _ in range(T):
    A = int(input())
    solve(A)