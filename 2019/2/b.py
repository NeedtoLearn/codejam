import sys
from random import randint

def solve():
    seen = {}
    for i in range(100):
        cur_day = int(input())
        if cur_day == -1:
            exit()
        if cur_day == 100:
            cur_min = 100
            cur_vase = 20
            for vase, cnt in seen.items():
                if cnt < cur_min:
                    cur_vase = vase
            print(cur_vase, 100)
            sys.stdout.flush()
        elif cur_day <= 95:
            print(i % 19 + 1, 100)
            sys.stdout.flush()
        else:
            vase = 20
            while vase in seen:
                vase = randint(1, 19)
            print(vase, 0)
            sys.stdout.flush()
            tokens = list(map(int, input().split()))
            seen[vase] = tokens[0]

T = int(input())
for _ in range(T):
    solve()
