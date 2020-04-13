def find_path(given_path):
    new_path = ''
    for d in given_path:
        new_path += 'E' if d == 'S' else 'S'
    return new_path

T = int(input())
for c in range(1, T + 1):
    N = int(input())
    ans = find_path(input())
    print('Case #{0}: {1}'.format(c, ans))
