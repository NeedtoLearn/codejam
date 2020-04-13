def solve(S):
    newS, opening = '', 0
    for d in map(int, S):
        if d > opening:
            newS += '(' * (d - opening)
        elif d < opening:
            newS += ')' * (opening - d)
        opening = d
        newS += str(d)
    return newS + ')' * opening


T = int(input())
for x in range(1, T + 1):
    S = input()
    y = solve(S)
    print('Case #{0}: {1}'.format(x, y))
