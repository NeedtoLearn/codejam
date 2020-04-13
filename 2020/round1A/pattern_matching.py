def solve(patterns):
    tokens, starts, ends = [], [], []
    for pattern in patterns:
        token = pattern.split('*')
        if token[0]:
            starts.append(token[0])
            token = token[1:]
        if token[-1]:
            ends.append(token[-1])
            token = token[:-1]
        tokens.append(token)
    # Check if starts and ends are valid
    starts.sort(key=len)
    for start in starts:
        if not starts[-1].startswith(start):
            return '*'
    ends.sort(key=len)
    for end in ends:
        if not ends[-1].endswith(end):
            return '*'
    return (starts[-1] if starts else '') + ''.join(''.join(token) for token in tokens) + (ends[-1] if ends else '')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    patterns = [input() for _ in range(N)]
    name = solve(patterns)
    print('Case #{0}: {1}'.format(t, name))
