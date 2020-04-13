import string
from math import sqrt

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(N, L, values):
    mid_point, com_div = -1, -1
    for i in range(1, len(values)):
        if values[i] != values[i-1]:
            mid_point = i
            com_div = gcd(values[i-1], values[i])

    # First half
    div = com_div
    first_half = []
    for i in range(mid_point - 1, -1, -1):
        div = values[i] // div
        first_half.append(div)
    first_half.reverse()

    # Second half
    div = com_div
    second_half = []
    for i in range(mid_point, len(values)):
        div = values[i] // div
        second_half.append(div)
    
    cipher_nums = first_half + [com_div] + second_half
    maps = dict(zip(sorted(set(cipher_nums)), string.ascii_uppercase))
    cipher_chars = [maps[num] for num in cipher_nums]
    return ''.join(cipher_chars)

T = int(input())
for c in range(1, T + 1):
    N, L = map(int, input().split())
    values = list(map(int, input().split()))
    ans = solve(N, L, values)
    print('Case #{0}: {1}'.format(c, ans)) 
