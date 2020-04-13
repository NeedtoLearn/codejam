# Precompute prime numbers for first 10000 numbers
is_prime = [True] * 10001
for d in range(2, 101):
    if is_prime[d]:
        for i in range(d * 2, 10001, d):
            is_prime[i] = False

primes = [i for i in range(1, 10001) if is_prime[i]]

# Solution
def find_prime_multiplier(N, value):
    for prime in primes:
        if value % prime == 0 and is_prime[value // prime]:
            return prime, value // prime

def combine_pairs(pairs):
    pass

def solve(N, L, values):
    pairs = [find_prime_multiplier(value) for value in values]
    numbers = combine_pairs(pairs)
    sorted_nums = sorted(set(numbers))
    indexes = [sorted_nums.index(value) for value in numbers]
    ans = [chr(ord('A') + idx) for idx in indexes]
    return ''.join(ans)

T = int(input())
for c in range(1, T + 1):
    N, L = map(int, input().split())
    values = list(map(int, input().split()))
    ans = solve(N, L, values)
    print('Case #{0}: {1}'.format(c, ans))  
