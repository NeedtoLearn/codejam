def is_stack_valid(ant_stack):
    cur_weight = 0
    for ant in reversed(ant_stack):
        if cur_weight > 6 * ant:
            return False
        cur_weight += ant
    return True

def stack_ants_recursive(N, ants, cur_stack):
    if N == 0:
        return len(cur_stack)
    # Check if next ant can climb up to cur_stack
    if not is_stack_valid(cur_stack + ants[:1]):
        return stack_ants_recursive(N-1, ants[1:], cur_stack)
    return max(
        stack_ants_recursive(N-1, ants[1:], cur_stack),
        stack_ants_recursive(N-1, ants[1:], cur_stack + ants[:1]))

def solve():
    T = int(input())
    for c in range(1, T + 1):
        N = int(input())
        ants = list(map(int, input().split()))
        ants.reverse()
        size = stack_ants_recursive(N, ants, [])
        print('Case #{0}: {1}'.format(c, size))

solve()
