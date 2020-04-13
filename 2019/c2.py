import string
from math import sqrt

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(N, L, values):
    if values[0] == values[1]:
        prev_div = sqrt(values[0])
        cipher_nums = [prev_div, prev_div]
    else:
        prev_div = gcd(values[0], values[1])
        cipher_nums = [values[0] // prev_div, prev_div]
    for i in range(1, len(values)):
        prev_div = values[i] // prev_div
        cipher_nums.append(prev_div)
    maps = dict(zip(sorted(set(cipher_nums)), string.ascii_uppercase))
    cipher_chars = [maps[num] for num in cipher_nums]
    return ''.join(cipher_chars)

T = int(input())
for c in range(1, T + 1):
    N, L = map(int, input().split())
    values = list(map(int, input().split()))
    ans = solve(N, L, values)
    print('Case #{0}: {1}'.format(c, ans)) 
